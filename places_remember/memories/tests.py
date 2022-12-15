from django.test import TestCase
from .models import Memory, Image, CustomUser


class MemoriesTestCase(TestCase):
    def test_create_memory(self):
        # create test_user
        user = CustomUser(username="test_user")
        user.save()
        # creare memory 1
        # save memory 1 in db
        memory_1 = Memory(
            name="memory_1",
            description="description_1",
            user_id=user,
        )
        memory_1.save()
        # create memory 2
        # save memory 2 in db
        memory_2 = Memory(
            name="memory_2",
            description="description_2",
            user_id=user,
        )
        memory_2.save()

        # load all memories from db and check if its amount equals to 2
        all_memories = Memory.objects.all()
        self.assertEqual(len(all_memories), 2)
        # check if the first loaded memory == memory 1 and the second one == memory 2
        self.assertEqual(all_memories[0].pk, memory_1.pk)
        self.assertEqual(all_memories[1].pk, memory_2.pk)


class ImageTestCase(TestCase):
    def test_create_image(self):
        # create test memory and test user
        user = CustomUser(username="test_user")
        user.save()
        # create memory 1
        # save memory 1 in db
        memory_1 = Memory(
            name="memory_1",
            description="description_1",
            user_id=user,
        )
        memory_1.save()
        # create two test images
        image_1 = Image(memory=memory_1, image="")
        image_1.save()

        image_2 = Image(memory=memory_1, image="")
        image_2.save()

        all_images = Image.objects.all()
        self.assertEqual(len(all_images), 2)

        self.assertEqual(all_images[0].pk, image_1.pk)
        self.assertEqual(all_images[1].pk, image_2.pk)
