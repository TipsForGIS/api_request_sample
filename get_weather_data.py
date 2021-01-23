import funcs

coords_file,output_file = funcs.sys_argv_valid()

if not funcs.input_file_exists(coords_file)[0]:
    print(funcs.input_file_exists(coords_file)[1])
else:
    if not funcs.input_file_valid(coords_file)[0]:
        print(funcs.input_file_valid(coords_file)[1])
    else:
        if not funcs.get_df_if_columns_valid(coords_file)[0]:
            print(funcs.get_df_if_columns_valid(coords_file)[1])
        else:
            coords_df = funcs.get_df_if_columns_valid(coords_file)[1]

            coords_df = funcs.update_df_temp(coords_df)
            coords_df = funcs.update_df_polt(coords_df)
            coords_df = funcs.update_df_elev(coords_df)
            
            coords_df.to_csv(output_file, index=False)
            



