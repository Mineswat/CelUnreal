import unreal
from datetime import datetime

now = datetime.now() # current date and time

time = now.strftime("%H:%M:%S")


class DenzelMaterialFactory():
    material_factory = unreal.MaterialFactoryNew() # Get the asset tools
    asset_tools = unreal.AssetToolsHelpers.get_asset_tools() # Define the material factory

    file_path = "/Game/Materials/Denzel"
    mat_name = "DenzelMaterial"

    def __init__(self):
        unreal.log(f"Denzel material factory has been created at {time}")

    


    def saveChanges(self,material):
        material = unreal.Material
        unreal.EditorAssetLibrary.save_asset(material.get_path_name())
        unreal.log(f"Changes have been saved for {material.getname}")

    def createMaterial(self,name=""):
        #if file exist then remove it 

        newMaterial = self.asset_tools.create_asset(name, self.file_path,unreal.Material,self.material_factory)

        unreal.log(F"{name} material has been created.")
        self.saveChanges(newMaterial) #save changes/apply changes

        return(newMaterial)
    
    def changeParamater(self,material,paramater=unreal.MaterialProperty.MP_BASE_COLOR,amount=unreal.LinearColor(4,0,0)):

        #detect if its a float or vector to convert the constant3vector


        base_color = unreal.MaterialEditingLibrary.create_material_expression(material, unreal.MaterialExpressionConstant3Vector, -384, 0)
        base_color.constant = amount
        unreal.MaterialEditingLibrary.connect_material_property(base_color, "", paramater)
        self.saveChanges(material)
        
    def saveChanges(self,material):
        unreal.EditorAssetLibrary.save_asset(material.get_path_name())
        unreal.log(f"Changes have been saved for ")




        


DMF = DenzelMaterialFactory()

MyMaterial = DMF.createMaterial("DenzelMaterial3")
DMF.changeParamater(MyMaterial)








    




