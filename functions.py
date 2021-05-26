import os
def user_path(User):
        
    if User=="Aurélien":
        path_to_train = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset','python','train')
        path_to_classnames = os.path.join('C:','\\Users','lyz50','Documents','GitHub','plantnet_dataset')
        path_to_folder=os.path.join('C:','\\Users','lyz50',"documents","Github","Projet-L3")
    elif User=="Guilhem":
        path_to_train = os.path.join('C:/','Plantnet_project','plantnet_subset')
        path_to_classnames = os.path.join('C:/','Plantnet_project')
        path_to_folder= os.path.join('C:','\\Users\guilh\OneDrive\Documents\GitHub\Projet-L3')
    elif User=="Joseph":
        path_to_train = os.path.join("/home","jsalmon","Documents","Datasets","train")
        path_to_classnames = os.path.join("/home","jsalmon","Documents","...")
        path_to_folder=os.path.join("...")
    elif User=="Camille":
        path_to_train = os.path.join("...")
        path_to_classnames = os.path.join("...")
        path_to_folder=os.path.join("...")
    return ((path_to_train,path_to_classnames,path_to_folder))