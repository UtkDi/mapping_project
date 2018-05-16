import classes.data_mapping_classes as dmpc
import sys
import csv
import ast


def read_commandline_inputs():
    input_file = dmpc.InputFiles(sys.argv[1], sys.argv[2], sys.argv[3])
    output_file = dmpc.OutputFile(sys.argv[4])
    return input_file, output_file


def read_master_brands_file(master_handle_file):
    with open(master_handle_file, 'r', newline='') as bf:
        csvf = csv.DictReader(bf, delimiter=',', quotechar='"')
        brand_list = load_brands(csvf)
        return brand_list


def load_brands(csv_reader):
    master_brands_list = []

    for row in csv_reader:
        print(row)
        temp_brand_object = dmpc.Brand(row['Unique Key'], row['Handle'])
        master_brands_list.append(temp_brand_object)

    return master_brands_list


def update_brand_follower_count(master_brands_list, brand_list_file):
    mapping_dict = map_master_brand_with_class_objects(master_brands_list)
    read_brand_list_file(brand_list_file, mapping_dict)


def map_master_brand_with_class_objects(master_brand_objects_list):
    mapping_dict = {}
    for each in master_brand_objects_list:
        mapping_dict[each.brand_handle] = each
    return mapping_dict


def read_brand_list_file(brand_list, mapping_dict):
    with open(brand_list, 'r', newline='') as bf:
        csvf = csv.DictReader(bf, delimiter=',', quotechar='"')
        load_brands_listing(csvf, mapping_dict)


def load_brands_listing(csv_reader, master_brands_dictionary):
    for row in csv_reader:
        brand = master_brands_dictionary[row['screen_name']]
        brand.followers_count = row['followers_count']


def read_post_table(post_table_file):
    with open(post_table_file, 'r', newline='') as bf:
        csvf = csv.DictReader(bf, delimiter=',', quotechar='"')
        post_list = load_posts(csvf)
        return post_list


def load_posts(csv_reader):
    posts_lists = []
    for row in csv_reader:
        temp_post_object = dmpc.Post(row['Master Key'], row['Dataset Key'], row['Segment Type'], row['Channel'], ast.literal_eval(row['Hashtag']),
                                     row['Handle'], row['Post Content'], int(row['Retweets']), int(row['Replies']), int(row['Likes']), row['Post Time'],
                                     row['Post Url'], row['Handle Image Url'])
        posts_lists.append(temp_post_object)

    return posts_lists


def map_the_post_to_brands(brand_mapping_dict, post_lists):
    for post in post_lists:
        if brand_mapping_dict.get(post.handle) is None:
            continue
        brand_object = brand_mapping_dict[post.handle]
        brand_object.posts_lists.append(post)

        for each in post.hashtag:
            brand_object.hashtags_dict[each] = 0


def update_the_impression_count(brand):
    for hashtag in brand.hashtags_dict:
        for post in brand.posts_lists:
            if hashtag in post.hashtag:
                brand.hashtags_dict[hashtag] += (post.retweets + post.replies + post.likes + (brand.followers_count * 0.4))
    return


def process_the_impression_count(brands_list):
    for each in brands_list:
        update_the_impression_count(each)


def write_data_to_file(out_file, brands_list):
    with open(out_file, 'w', newline='', encoding='utf-16') as csv_file:
        csvf = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for brand in brands_list:
            for hashtag, value in brand.hashtags_dict.items():
                csvf.writerow([brand.unique_key, None, 'brand', 'weibo', hashtag, value])
    return
