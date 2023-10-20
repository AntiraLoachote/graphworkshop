from rest_framework import status
from rest_framework.test import APITestCase
from user_manager.models import User, Node, Author
from post_manager.models import Post, Comment
from django.urls import reverse


class NodeViewsetTest(APITestCase):
    def setUp(self):
        self.user = User.objects.create()
        self.author = Author.objects.create(user=self.user, node=Node.objects.create())
        self.post = Post.objects.create(owner=self.author, node=Node.objects.create(), text='hello world')
        self.comment = Comment.objects.create(
            node=Node.objects.create(), owner=self.author, post=self.post
        )

    def test_get_node(self):
        post_node = self.post.node.id
        self.url = reverse("v1:node-detail", kwargs={"pk": post_node})

        self.response = self.client.get(self.url, {"fields": "text,owner"})

        self.assertEqual(self.response.status_code, status.HTTP_200_OK)
        self.assertEqual(self.response.data, {
            'text': self.post.text,
            'owner': self.author.id
        })
