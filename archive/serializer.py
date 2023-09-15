from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth import get_user_model


User = get_user_model()


class OwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("id", "username")


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = (
            "id",
            "title",
        )


class PostSerializer(serializers.ModelSerializer):
    owner = serializers.HyperlinkedIdentityField(many=False, view_name="owner-detail")
    comments = serializers.HyperlinkedRelatedField(
        many=True, view_name="comment-detail", queryset=Comment.objects.all()
    )

    class Meta:
        model = Post
        fields = (
            "title",
            "owner",
            "custom_id",
            "category",
            "publish_date",
            "last_updated",
            "comments",
        )
