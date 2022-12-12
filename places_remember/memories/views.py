from django.views.generic import (
    ListView,
    CreateView,
    DetailView,
    UpdateView,
    DeleteView,
)
from django.urls import reverse_lazy
from .forms import AddMemoryForm
from .models import Memory
from .forms import ImageFormset
from django.shortcuts import redirect
from django.http import Http404


class ObjectViewMixin:
    model = None
    allow_empty = False

    def get(self, request, *args, **kwargs):
        if self.request.user.is_authenticated:
            self.object = self.get_object(
                self.model.objects.filter(user_id=request.user)
            )
        else:
            raise Http404("Page not found")
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class MemoryListView(ListView):
    model = Memory
    context_object_name = "memories"
    allow_empty = False

    def get_queryset(self):
        if self.request.user.is_authenticated:
            return Memory.objects.filter(user_id=self.request.user)
        return Memory.objects.none()


class MemoryCreateView(ObjectViewMixin, CreateView):
    model = Memory
    form_class = AddMemoryForm
    success_url = reverse_lazy("memories:memories")

    def get_context_data(self, **kwargs):
        context = super(MemoryCreateView, self).get_context_data(**kwargs)
        if self.request.POST:
            context["image_formset"] = ImageFormset(self.request.POST)
        else:
            context["image_formset"] = ImageFormset()
        return context

    def post(self, request, *args, **kwargs):
        self.object = None
        form_class = self.get_form_class()
        form = self.get_form(form_class)
        image_formset = ImageFormset(self.request.POST)
        if form.is_valid() and image_formset.is_valid():
            return self.form_valid(form, image_formset)
        return self.form_invalid(form, image_formset)

    def form_valid(self, form, image_formset):
        self.object = form.save(commit=False)
        self.object.user_id = self.request.user
        self.object.save()

        images = image_formset.save(commit=False)
        print("IMAGES", images)

        for image in images:
            image.image = self.object
            image.save()
        return redirect(self.success_url)

    def form_invalid(self, form, image_formset):
        return self.render_to_response(
            self.get_context_data(form=form, image_formset=image_formset)
        )


class MemoryDetailView(ObjectViewMixin, DetailView):
    model = Memory
    context_object_name = "memory"
    pk_url_kwarg = "pk"


class MemoryDeleteView(ObjectViewMixin, DeleteView):
    model = Memory
    success_url = reverse_lazy("memories:memories")


class MemoryUpdateView(ObjectViewMixin, UpdateView):
    model = Memory
    form_class = AddMemoryForm
    success_url = reverse_lazy("memories:memories")
    context_object_name = "memory"
