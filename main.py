import data_mapping as dmp

if __name__=="__main__":
    input_files, output_file = dmp.read_commandline_inputs()

    brands_list = dmp.read_master_brands_file(input_files.master_handle_file)

    dmp.update_brand_follower_count(brands_list, input_files.brand_list_file)

    post_list = dmp.read_post_table(input_files.post_table_file)

    brand_mapping_dict = dmp.map_master_brand_with_class_objects(brands_list)

    dmp.map_the_post_to_brands(brand_mapping_dict, post_list)

    print(brand_mapping_dict)

    dmp.process_the_impression_count(brands_list)

    dmp.write_data_to_file(output_file.file_name, brands_list)