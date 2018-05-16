class Brand:
    def __init__(self,unique_key, brand_handle):
        self.unique_key = unique_key
        self.brand_handle = brand_handle
        self.followers_count = 0
        self.posts_lists = []
        self.hashtags_dict = {}

    def __str__(self):
        return self.unique_key+'|'+self.brand_handle+'|'+str(self.followers_count)


class Post:
    def __init__(self, master_key, dataset_key, segment_type, channel, hashtag,
                 handle, post_content, retweets, replies, likes, post_time, post_url, handle_image_url):
        self.master_key = master_key
        self.dataset_key = dataset_key
        self.segment_type = segment_type
        self.channel = channel
        self.hashtag = hashtag
        self.handle = handle
        self.post_content = post_content
        self.retweets = retweets
        self.replies = replies
        self.likes = likes
        self.post_time = post_time
        self.post_url = post_url
        self.handle_image_url = handle_image_url


class HashtagRow:
    def __init__(self, unique_key, hashtag, impression):
        self.unique_key = unique_key
        self.hashtag = hashtag
        self.impression = impression


class InputFiles:
    def __init__(self, file1, file2, file3):
        self.master_handle_file = file1
        self.brand_list_file = file2
        self.post_table_file = file3


class OutputFile:
    def __init__(self, file1):
        self.file_name = file1
        self.open_mode = None
