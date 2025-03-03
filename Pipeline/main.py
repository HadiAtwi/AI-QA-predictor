from Pipeline import Pipeline

if __name__ == "__main__":
    pipeline = Pipeline(
        exe_path="C:\\Users\\hatwi\\OneDrive - Expleo France\\Atwi_Hadi\\Thesis development environment\\Backward_Slicer_C#\\EXE for SLXReader\\bin\\Debug\\EXE for SLXReader.exe",
        slx_path="C:\\Users\\hatwi\\Documents\\Thesis development environment\\Data Preparation\\new dev\\NVEM2.slx",
        findings_list="C:\\Users\\hatwi\\Documents\\Thesis development environment\\Data Preparation\\new dev\\SLDV_NVEM2_CL6.json",
        rf_model_path="rf_model.pkl",
        mlp_model_path="sequential_model.pth"
    )
    pipeline.run(create_from_scratch=True, use_rf=True, use_mlp=False)
