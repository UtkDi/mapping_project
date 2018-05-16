import data_mapping as dmp

if __name__=="__main__":
    # Read command line arguments
    input_files, output_file = dmp.read_commandline_inputs()

    # Load all the brand names from brand master file
    brands_list = dmp.read_master_brands_file(input_files.master_handle_file)
    # Map the brand objects with their brand name
    brand_mapping_dict = dmp.map_master_brand_with_class_objects(brands_list)

    # Update the followers of the brand from the brand_list file
    dmp.update_brand_follower_count(brands_list, input_files.brand_list_file)

    # Load the post data from post_table file
    post_list = dmp.read_post_table(input_files.post_table_file)

    # Map the posts to their respective brands
    dmp.map_the_post_to_brands(brand_mapping_dict, post_list)

    # Process the impression count for all the brand and hashtags
    dmp.process_the_impression_count(brands_list)

    # Write the final data to the output file
    dmp.write_data_to_file(output_file.file_name, brands_list)