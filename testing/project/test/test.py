from unittest import TestCase, main
from project.social_media import SocialMedia


class TestSocialMediaClass(TestCase):
    def setUp(self):
        self.user = SocialMedia('user123', 'Instagram', 1000, 'photo')

    def test_social_media_structure(self):
        self.assertEqual(SocialMedia.__base__.__name__, "object")
        self.assertTrue(hasattr(SocialMedia, "_validate_and_set_platform"))
        self.assertTrue(hasattr(SocialMedia, "create_post"))
        self.assertTrue(hasattr(SocialMedia, "like_post"))
        self.assertTrue(hasattr(SocialMedia, "comment_on_post"))

        self.assertTrue(isinstance(getattr(SocialMedia, "platform"), property))
        self.assertTrue(isinstance(getattr(SocialMedia, "followers"), property))

    def test_initialization(self):
        self.assertEqual(self.user._username, 'user123')
        self.assertEqual(self.user._platform, 'Instagram')
        self.assertEqual(self.user._followers, 1000)
        self.assertEqual(self.user._content_type, 'photo')
        self.assertEqual(self.user._posts, [])

    def test_platform_setter_valid(self):
        valid_platforms = ['Instagram', 'YouTube', 'Twitter']
        for platform in valid_platforms:
            with self.subTest(platform=platform):
                self.user.platform = platform
                self.assertEqual(self.user.platform, platform)

    def test_platform_setter_invalid(self):
        invalid_platform = 'InvalidPlatform'
        with self.assertRaises(ValueError) as context:
            self.user.platform = invalid_platform
        self.assertEqual(str(context.exception), "Platform should be one of ['Instagram', 'YouTube', 'Twitter']")

    def test_followers_setter_valid(self):
        self.user.followers = 2000
        self.assertEqual(self.user.followers, 2000)

    def test_followers_setter_invalid(self):
        with self.assertRaises(ValueError) as context:
            self.user.followers = -100
        self.assertEqual(str(context.exception), "Followers cannot be negative.")

    def test_create_post(self):
        result = self.user.create_post("Awesome photo!")
        self.assertEqual(result, "New photo post created by user123 on Instagram.")
        self.assertEqual(len(self.user._posts), 1)

    def test_like_post_within_limit(self):
        self.user.create_post("Awesome photo!")
        result = self.user.like_post(0)
        self.assertEqual(result, "Post liked by user123.")
        self.assertEqual(self.user._posts[0]['likes'], 1)

    def test_like_post_reached_limit(self):
        self.user.create_post("Awesome photo!")
        for _ in range(10):
            self.user.like_post(0)
        result = self.user.like_post(0)
        self.assertEqual(result, "Post has reached the maximum number of likes.")
        self.assertEqual(self.user._posts[0]['likes'], 10)

    def test_like_post_invalid_index(self):
        result = self.user.like_post(0)
        self.assertEqual(result, "Invalid post index.")

    def test_comment_on_post_valid(self):
        self.user.create_post("Awesome photo!")
        result = self.user.comment_on_post(0, "Great shot!")
        self.assertEqual(result, "Comment added by user123 on the post.")
        self.assertEqual(len(self.user._posts[0]['comments']), 1)

    def test_comment_on_post_invalid_comment(self):
        self.user.create_post("Awesome photo!")
        result = self.user.comment_on_post(0, "Nice!")
        self.assertEqual(result, "Comment should be more than 10 characters.")
        self.assertEqual(len(self.user._posts[0]['comments']), 0)


if __name__ == '__main__':
    main()
