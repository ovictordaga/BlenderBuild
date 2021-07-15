
# import bpy chama a API do blender para python e o print gera o espaçamento para uma melhor visualização no console
import bpy
print("------\n")


 
 # Define render engine
scn = bpy.context.scene
if not scn.render.engine == 'CYCLES':
    scn.render.engine = 'CYCLES'

#Classe responsável pela lista e endereçamento das peças(ADICIONAR NOVAS PEÇAS NESTA CLASSE)
class pecas(object):
        
    lista_pecas = ("snowboard_small", "plate_2x2_eye", "plate_1x1_eye", "brick_2x2_inverted_ball", "usb_hub_bot","usb_hub", "usb_hub_top", "tire_30", "medium_motor", "sensor_motion", "sensor_tilt", "converter_angled_1",          "wheel_14_axle", "lever", "plate_2x2_round_up", "plate_1x2_2x2", "plate_1x2", "plate_1x4", "plate_1x6","plate_1x12", "gear_rack", "brick_1x1_stud_1", "round_1x1_yellow", "round_1x1_red", "pulley_belt_wheel","brick_2x2_round", "brick_1x6_curved_blue", "round_1x1_green", "gearbox", "gear_worm", "axle_connector","axle_3", "axle_7", "bush", "bush_half", "plate_2x3_round_hole", "plate_4x4_quarter", "plate_1x8_flat",             "brick_1x2x2_slope", "brick_1x2_pin", "converter_angled_3", "plate_4x4_round", "plate_1x2_flat","brick_1x4_curved_double", "brick_1x2", "brick_1x4", "brick_2x2_black", "brick_2x4_blue", "ball_joint_technic","plate_2x6", "plate_2x4", "brick_1x2_inverted_slope", "brick_3x1_slope", "brick_half_1x2_slope",                    "brick_2x4_orange", "gear_24", "gear_8", "axle_4_stop", "chain_21", "plate_2x2_round_hole", "technic_reel_3x2","brick_1x2_axle", "brick_2x2_ball", "converter_angled_4", "plate_4x6_corner", "brick_3x1_slope_inverted","bric,k_1x2_slope", "brick_1x16_h", "brick_1x12_h", "brick_1x8_h", "brick_1x4_h", "brick_1x2_h","brick_1x6_curved", "brick_1x3_curved", "axle_2", "flower_2_2x2", "element_seperator", "tube_connector","beam_3x5L", "beam_1x7", "plate_2x2_round", "stem_plant", "flower_1_2x2", "gear_20_bevel_slim", "connector_axle","belt_wheel_tire", "gear_20_bevel", "gear_12_bevel", "connector_axle_2", "rubber_double_connector", "connector_friction",       "axle_10", "axle_6", "tire_37", "plate_2x2_rounded_bottom", "plate_1x1_round", "pin_connector_plate","plate_2x16", "plate_2x8", "turntable_4x4", "brick_1x2_slope_green", "brick_1x2_slope","brick_2x2_blue","brick_2x2_2balls","motor_nucleus" )

    axle_10 = lista_pecas.index("axle_10")
    axle_2 = lista_pecas.index("axle_2")
    axle_3 = lista_pecas.index("axle_3")
    axle_4_stop = lista_pecas.index("axle_4_stop")
    axle_6 = lista_pecas.index("axle_6")
    axle_7 = lista_pecas.index("axle_7")
    axle_connector = lista_pecas.index("axle_connector")
    ball_joint_technic = lista_pecas.index("ball_joint_technic")
    beam_1x7 = lista_pecas.index("beam_1x7")
    beam_3x5L = lista_pecas.index("beam_3x5L")
    belt_wheel_tire = lista_pecas.index("belt_wheel_tire")
    brick_1x1_stud_1 = lista_pecas.index("brick_1x1_stud_1")
    brick_1x12_h = lista_pecas.index("brick_1x12_h")
    brick_1x16_h = lista_pecas.index("brick_1x16_h")
    brick_1x2 = lista_pecas.index("brick_1x2")
    brick_1x2_axle = lista_pecas.index("brick_1x2_axle")
    brick_1x2_h = lista_pecas.index("brick_1x2_h")
    brick_1x2_inverted_slope = lista_pecas.index("brick_1x2_inverted_slope")
    brick_1x2_pin = lista_pecas.index("brick_1x2_pin")
    brick_1x2_slope = lista_pecas.index("brick_1x2_slope")
    brick_1x2_slope_green = lista_pecas.index("brick_1x2_slope_green")
    brick_1x2x2_slope = lista_pecas.index("brick_1x2x2_slope")
    brick_1x3_curved = lista_pecas.index("brick_1x3_curved")
    brick_1x4 = lista_pecas.index("brick_1x4")
    brick_1x4_curved_double = lista_pecas.index("brick_1x4_curved_double")
    brick_1x4_h = lista_pecas.index("brick_1x4_h")
    brick_1x6_curved = lista_pecas.index("brick_1x6_curved")
    brick_1x6_curved_blue = lista_pecas.index("brick_1x6_curved_blue")
    brick_1x8_h = lista_pecas.index("brick_1x8_h")
    brick_2x2_2balls = lista_pecas.index("brick_2x2_2balls")
    brick_2x2_ball = lista_pecas.index("brick_2x2_ball")
    brick_2x2_black = lista_pecas.index("brick_2x2_black")
    brick_2x2_blue = lista_pecas.index("brick_2x2_blue")
    brick_2x2_inverted_ball = lista_pecas.index("brick_2x2_inverted_ball")
    brick_2x2_round = lista_pecas.index("brick_2x2_round")
    brick_2x4_blue = lista_pecas.index("brick_2x4_blue")
    brick_2x4_orange = lista_pecas.index("brick_2x4_orange")
    brick_3x1_slope = lista_pecas.index("brick_3x1_slope")
    brick_3x1_slope_inverted = lista_pecas.index("brick_3x1_slope_inverted")
    brick_half_1x2_slope = lista_pecas.index("brick_half_1x2_slope")
    bush_half = lista_pecas.index("bush_half")
    bush = lista_pecas.index("bush")
    chain_21 = lista_pecas.index("chain_21") 
    connector_axle = lista_pecas.index("connector_axle")
    connector_axle_2 = lista_pecas.index("connector_axle_2")
    connector_friction = lista_pecas.index("connector_friction")
    converter_angled_1 = lista_pecas.index("converter_angled_1")
    converter_angled_3 = lista_pecas.index("converter_angled_3")
    converter_angled_4 = lista_pecas.index("converter_angled_4")
    element_seperator = lista_pecas.index("element_seperator")
    flower_1_2x2 = lista_pecas.index("flower_1_2x2")
    flower_2_2x2 = lista_pecas.index("flower_2_2x2")
    gear_12_bevel = lista_pecas.index("gear_12_bevel")
    gear_20_bevel = lista_pecas.index("gear_20_bevel")
    gear_20_bevel_slim = lista_pecas.index("gear_20_bevel_slim")
    gear_24 = lista_pecas.index("gear_24")
    gear_8 = lista_pecas.index("gear_8")
    gear_rack = lista_pecas.index("gear_rack")
    gear_worm = lista_pecas.index("gear_worm")
    gearbox = lista_pecas.index("gearbox")
    lever = lista_pecas.index("lever")
    medium_motor = lista_pecas.index("medium_motor")
    pin_connector_plate = lista_pecas.index("pin_connector_plate")
    plate_1x1_eye = lista_pecas.index("plate_1x1_eye")
    plate_1x1_round = lista_pecas.index("plate_1x1_round")
    plate_1x12 = lista_pecas.index("plate_1x12")
    plate_1x2 = lista_pecas.index("plate_1x2")
    plate_1x2_2x2 = lista_pecas.index("plate_1x2_2x2")
    plate_1x2_flat = lista_pecas.index("plate_1x2_flat")
    plate_1x4 = lista_pecas.index("plate_1x4")
    plate_1x6 = lista_pecas.index("plate_1x6")
    plate_1x8_flat = lista_pecas.index("plate_1x8_flat")
    plate_2x16 = lista_pecas.index("plate_2x16")
    plate_2x2_eye = lista_pecas.index("plate_2x2_eye")
    plate_2x2_round = lista_pecas.index("plate_2x2_round")
    plate_2x2_round_hole = lista_pecas.index("plate_2x2_round_hole")
    plate_2x2_round_up = lista_pecas.index("plate_2x2_round_up")
    plate_2x2_rounded_bottom = lista_pecas.index("plate_2x2_rounded_bottom")
    plate_2x3_round_hole = lista_pecas.index("plate_2x3_round_hole")
    plate_2x4 = lista_pecas.index("plate_2x4")
    plate_2x6 = lista_pecas.index("plate_2x6")
    plate_2x8 = lista_pecas.index("plate_2x8")
    plate_4x4_quarter = lista_pecas.index("plate_4x4_quarter")
    plate_4x4_round = lista_pecas.index("plate_4x4_round")
    plate_4x6_corner = lista_pecas.index("plate_4x6_corner")
    pulley_belt_wheel = lista_pecas.index("pulley_belt_wheel")
    round_1x1_green = lista_pecas.index("round_1x1_green")
    round_1x1_red = lista_pecas.index("round_1x1_red")
    round_1x1_yellow = lista_pecas.index("round_1x1_yellow")
    rubber_double_connector = lista_pecas.index("rubber_double_connector")
    sensor_motion = lista_pecas.index("sensor_motion")
    sensor_tilt = lista_pecas.index("sensor_tilt")
    snowboard_small = lista_pecas.index("snowboard_small")
    stem_plant = lista_pecas.index("stem_plant")
    technic_reel_3x2 = lista_pecas.index("technic_reel_3x2")
    tire_30 = lista_pecas.index("tire_30")
    tire_37 = lista_pecas.index("tire_37")
    tube_connector = lista_pecas.index("tube_connector")
    turntable_4x4 = lista_pecas.index("turntable_4x4")
    usb_hub = lista_pecas.index("usb_hub")
    usb_hub_bot = lista_pecas.index("usb_hub_bot")
    usb_hub_top = lista_pecas.index("usb_hub_top")
    wheel_14_axle = lista_pecas.index("wheel_14_axle")
    motor_nucleus = lista_pecas.index("motor_nucleus")
    print(axle_2)
        

###--------------------------------------Layout panels----------------------------------#
# As classe com o parametro bpy.types.Panel, são responsáveis por definir o visual e a localização dos menus.
#bl_label: Define o nome que aparecerá no painel 
#bl_space_type: Define o espaço onde o painel aparecerá, lembrando que esta é a primeira categoria hierarquica sendo que o nome 
#   tem que estar entre aspas e identico a tag do programa. 
#   Por exemplo PROPERTIES tem que ser escrito em  caps. Properties é um dos menus principais do programa
#bl_region_type: Determina qual o tipo de menu que será criado OLHAR COM MAIS ATENÇÂO ESTE TOPICO
#bl_context: Dentro do menu ja selecionado em space_type, ele define agora a aba ou sub-menu, novamente entre aspas e o nome identico a tag.



class Connectors(bpy.types.Panel):
    bl_label = "Connectors"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"
    
    
    def draw(self, context):
        layout = self.layout
 
        layout.label("Connectors",icon = "PINNED")
        row = layout.row(align=False)
        row.alignment = 'LEFT'
        row.operator("my.button", text="Pin").number = pecas.connector_friction
        row.operator("my.button", text="Pin-axle").number= pecas.connector_axle
        row.operator("my.button", text="Pin-axle ext.").number= pecas.connector_axle_2

class Eixos(bpy.types.Panel):
    bl_label = "Cross axle"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"
    
    
    def draw(self, context):
        layout = self.layout
 
        layout.label("Cross axle",icon = "PLUS")
        row = layout.row(align=True)
        row.alignment = 'EXPAND'
        row.operator("my.button", text="2").number = pecas.axle_2
        row.operator("my.button", text="3").number= pecas.axle_3
        row.operator("my.button", text="4 w/ stop").number= pecas.axle_4_stop
        row.operator("my.button", text="6").number= pecas.axle_6
        row.operator("my.button", text="7").number= pecas.axle_7
        row.operator("my.button", text="10").number= pecas.axle_10
        
        layout.label("Bush")
        row = layout.row(align=False)
        row.alignment = 'LEFT'
        row.operator("my.button", text=" Half").number= pecas.bush_half
        row.operator("my.button", text="Bush").number= pecas.bush
        
        
        
class engrenagens(bpy.types.Panel):
    bl_label = "Gears and Acessories"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"

    def draw(self, context):
        layout = self.layout
 
        layout.label("Gears",icon = "SCRIPTWIN")
        row = layout.row(align=False)
        row.alignment = 'LEFT'
        row.operator("my.button", text="8").number= pecas.gear_8
        row.operator("my.button", text="12").number= pecas.gear_12_bevel
        row.operator("my.button", text="20").number= pecas.gear_20_bevel
        row.operator("my.button", text="20 Slim").number= pecas.gear_20_bevel_slim
        row.operator("my.button", text="24").number= pecas.gear_24
        
        layout.label("Miscellaneous", icon = "SPLITSCREEN")
        row = layout.row(align=False)
        row.operator("my.button", text="Pulley").number= pecas.pulley_belt_wheel
        row.operator("my.button", text="Worm").number= pecas.gear_worm
        row.operator("my.button", text="Rack").number= pecas.gear_rack
        row.operator("my.button", text="Gearbox").number= pecas.gearbox
        

class technic_bricks(bpy.types.Panel):
    bl_label = "Technic Bricks & More"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"
    
    def draw(self, context):
        layout = self.layout
    
        layout.label("Technic Bricks",icon = "NLA")
        row = layout.row(align=False)
        row.operator("my.button", text="1x2").number= pecas.brick_1x2_h
        row.operator("my.button", text="1x2 Cross").number= pecas.brick_1x2_axle
        row.operator("my.button", text="1x2 Pin").number= pecas.brick_1x2_pin
        row = layout.row(align=False)
        row.operator("my.button", text="1x4").number= pecas.brick_1x4_h
        row.operator("my.button", text="1x8").number= pecas.brick_1x8_h
        row.operator("my.button", text="1x12").number= pecas.brick_1x12_h 
        row = layout.row(align=False)
        row.operator("my.button", text="1x16").number= pecas.brick_1x16_h
        row.operator("my.button", text="1x7 Tec.").number= pecas.beam_1x7
        row.operator("my.button", text="3x5 L Tec.").number= pecas.beam_3x5L
    


class adapters_converters(bpy.types.Panel):
    bl_label = "Adapters and Converters"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"
    
    def draw(self, context):
        layout = self.layout
    
        layout.label("Adapters and Converters",icon = "PHYSICS")
       
        row = layout.row(align=False)
        row.operator("my.button", text="Angled #1").number= pecas.converter_angled_1
        row.operator("my.button", text="Angled #3").number= pecas.converter_angled_3
        row.operator("my.button", text="Angled #4").number= pecas.converter_angled_4
        
        row = layout.row(align=False)
        row.operator("my.button", text="Axle connector").number= pecas.axle_connector
        row.operator("my.button", text="Pin connector").number= pecas.tube_connector
        
        row = layout.row(align=False)
        row.operator("my.button", text=" Rubber 2 axle").number= pecas.rubber_double_connector
        row.operator("my.button", text="Connector plate").number= pecas.pin_connector_plate
       
class eletronics(bpy.types.Panel):
    bl_label = "Eletronics"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"
    
    def draw(self, context):

        layout = self.layout
        
        layout.label("Eletronics",icon = "PLUGIN")
        row = layout.row(align=False)
        row.operator("eletric.button", text="Motor Nucleus").number= 0
        row.operator("eletric.button", text="Hub").number= 1
        row.operator("eletric.button", text="Hub top").number= 2  
        row = layout.row(align=False)
        row.operator("eletric.button", text="Medium Motor").number= 3
        row.operator("eletric.button", text="Motion sensor").number= 4
        row.operator("eletric.button", text="Tilt sensor").number= 5 
        
#Tools de eletric button Operator
class eletric_button(bpy.types.Operator):
    bl_idname = "eletric.button"
    bl_label = "Button"
    number = bpy.props.IntProperty()
    
    def execute(self, context):
        if self.number == 0:
            blendfile = "C:/Users/victor.daga/Documents/Montagens_Lego/cena_pecas/wedo_pieces_v1.7.blend"
                       
            section = "\\Object\\"
            object = "motor_nucleus"
            print (object)  
            
            bpy.ops.wm.append(
            filepath=blendfile + section + object, 
            filename=object  ,
            directory=blendfile + section)

        elif self.number == 1:
            
            blendfile ="C:/Users/victor.daga/Documents/Montagens_Lego/cena_pecas/wedo_pieces_v1.7.blend"
            section = "\\Group\\"
            object = 'Hub_group'
 
                
            bpy.ops.wm.append(filepath=blendfile + section + object, 
            filename=object,
            directory=blendfile + section)
            bpy.ops.group.objects_remove_all()

            bpy.context.scene.objects.active = bpy.data.objects["usb_hub_bot"]
            bpy.ops.object.select_grouped(extend=False, type='GROUP')
            bpy.ops.group.objects_remove_all()

        elif self.number == 2:
            blendfile = "C:/Users/victor.daga/Documents/Montagens_Lego/cena_pecas/wedo_pieces_v1.7.blend"
            section = "\\Object\\"
            object = "usb_hub_top"
            
                
            bpy.ops.wm.append(
            filepath=blendfile + section + object, 
            filename=object  ,
            directory=blendfile + section)

              
        elif self.number == 3:
            blendfile =  "C:/Users/victor.daga/Documents/Montagens_Lego/cena_pecas/wedo_pieces_v1.7.blend"
                    
            section = "\\Group\\"
            object = 'Motor_group'
 
                
            bpy.ops.wm.append(filepath=blendfile + section + object, 
            filename=object,
            directory=blendfile + section)

            bpy.context.scene.objects.active = bpy.data.objects["empty_motor1"]
            bpy.ops.object.select_grouped(extend=False, type='GROUP')
            bpy.ops.group.objects_remove_all()
            
        elif self.number == 4:
            blendfile =  "C:/Users/victor.daga/Documents/Montagens_Lego/cena_pecas/wedo_pieces_v1.7.blend"
                    
            section = "\\Group\\"
            object = 'Motion_sensor_group '
 
                
            bpy.ops.wm.append(filepath=blendfile + section + object, 
            filename=object,
            directory=blendfile + section)

            bpy.context.scene.objects.active = bpy.data.objects["empty_motion1"]
            bpy.ops.object.select_grouped(extend=False, type='GROUP')
            bpy.ops.group.objects_remove_all()

            

        elif self.number == 5:
            blendfile =  "C:/Users/victor.daga/Documents/Montagens_Lego/cena_pecas/wedo_pieces_v1.7.blend"
                    
            section = "\\Group\\"
            object = 'Tilt_sensor_group'
 
                
            bpy.ops.wm.append(filepath=blendfile + section + object, 
            filename=object,
            directory=blendfile + section)

            bpy.context.scene.objects.active = bpy.data.objects["empty_tilt1"]
            bpy.ops.object.select_grouped(extend=False, type='GROUP')
            bpy.ops.group.objects_remove_all()


        return{'FINISHED'} 
    
    
class Plates(bpy.types.Panel):
    bl_label = "Plates"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"
    
    def draw(self, context):
        layout = self.layout
        
        layout.label("Plates 1 x X", icon = "SPLITSCREEN")
        row = layout.row(align=False)
        row.operator("my.button", text="1x1").number= pecas.plate_1x1_round
        row.operator("my.button", text="1x2").number= pecas.plate_1x2
        row.operator("my.button", text="1x4").number= pecas.plate_1x4  
        row.operator("my.button", text="1x6").number= pecas.plate_1x6  
        row.operator("my.button", text="1x12").number= pecas.plate_1x12
        
        layout.label("Plates 2 x X", icon = "SPLITSCREEN")
        row = layout.row(align=False)
        row.operator("my.button", text="2x4").number= pecas.plate_2x4
        row.operator("my.button", text="2x6").number= pecas.plate_2x6
        row.operator("my.button", text="2x8").number= pecas.plate_2x8  
        row.operator("my.button", text="2x16").number= pecas.plate_2x16
        
        layout.label("Tile", icon = "SORTSIZE")
        row = layout.row(align=False)
        
        row.operator("my.button", text="1x2").number= pecas.plate_1x2_flat  
        row.operator("my.button", text="1x2 Slope").number= pecas.brick_half_1x2_slope
        row.operator("my.button", text="1x8").number= pecas.plate_1x8_flat  
        row.operator("my.button", text="2x2 up").number= pecas.plate_2x2_round_up
        row.operator("my.button", text="2x2 down").number= pecas.plate_2x2_round_hole
        
        
        layout.label("Miscellaneous", icon = "MAT_SPHERE_SKY")
        
        row = layout.row(align=False) 
        row.operator("my.button", text="L bracket").number= pecas.plate_1x2_2x2
        row.operator("my.button", text="3x2 hole").number= pecas.plate_2x3_round_hole
        row.operator("my.button", text="4x4 hole").number= pecas.plate_4x4_quarter  
        
        row = layout.row(align=False)
        row.operator("my.button", text="4x4 round").number= pecas.plate_4x4_round
        row.operator("my.button", text="2x2 round").number= pecas.plate_2x2_round
        
        row = layout.row(align=False)
        row.operator("my.button", text="2x2 bot").number= pecas.plate_2x2_rounded_bottom
        row.operator("my.button", text="4x6 trapeze").number= pecas.plate_4x6_corner
        
class bricks(bpy.types.Panel):
    bl_label = "Bricks"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"
    
    def draw(self, context):
        layout = self.layout
    
        layout.label("Classical Bricks", icon = "SPLITSCREEN")
        row = layout.row(align=False)
        row.operator("my.button", text="1x1").number= pecas.brick_1x1_stud_1
        row.operator("my.button", text="1x2").number= pecas.brick_1x2
        row.operator("my.button", text="1x4").number= pecas.brick_1x4
        row = layout.row(align=False)
        row.operator("my.button", text="2x2 Black").number= pecas.brick_2x2_black
        row.operator("my.button", text="2x2 Blue").number= pecas.brick_2x2_blue
        row = layout.row(align=False)
        row.operator("my.button", text="2x4 Oran").number= pecas.brick_2x4_orange
        row.operator("my.button", text="2x4 Blue").number= pecas.brick_2x4_blue
        
        layout.label("Round", icon = "ANTIALIASED")
        row = layout.row(align=False)
        row.operator("my.button", text="2x2 Round").number= pecas.brick_2x2_round
        row.operator("my.button", text="1x4 Arc.").number= pecas.brick_1x4_curved_double
        row.operator("my.button", text="1x3 Arc.").number= pecas.brick_1x3_curved
        
        row = layout.row(align=False)
        row.operator("my.button", text="1x6 Arc. Green").number= pecas.brick_1x6_curved
        row.operator("my.button", text="1x6 Arc. Blue").number= pecas.brick_1x6_curved_blue
        
        
        layout.label("Slope", icon = "IMAGE_ALPHA")
        row = layout.row(align=False)
        row.operator("my.button", text="2x1 Black").number= pecas.brick_1x2_slope
        row.operator("my.button", text="2x1 Green").number= pecas.brick_1x2_slope_green
        row.operator("my.button", text="3x1 Orange").number= pecas.brick_3x1_slope
        row.operator("my.button", text="2x1x2 Gray").number= pecas.brick_1x2x2_slope
        row = layout.row(align=False)
        row.operator("my.button", text="2x1 Inv.").number= pecas.brick_1x2_inverted_slope
        row.operator("my.button", text="3x1 Inv.").number= pecas.brick_3x1_slope_inverted
        
       
        layout.label("Articulated", icon = "FILE_PARENT")
        row = layout.row(align=False)
        row.operator("my.button", text="2x2 Ball").number= pecas.brick_2x2_ball
        row.operator("my.button", text="2x2 B.Plug").number= pecas.brick_2x2_inverted_ball
        row.operator("my.button", text="2x2 Double B.").number= pecas.brick_2x2_2balls
        row.operator("my.button", text="1x1 Ball").number= pecas.ball_joint_technic

class miscellaneous(bpy.types.Panel):
    bl_label = "Miscellaneous Parts"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"
    
    def draw(self, context):
        layout = self.layout
    
        layout.label("Miscellaneous", icon = "ACTION")
        row = layout.row(align=False)
        row.operator("my.button", text="Chain").number= pecas.chain_21
        row.operator("my.button", text="Y Tank").number= pecas.round_1x1_yellow
        row.operator("my.button", text="G Tank").number= pecas.round_1x1_green  
        row.operator("my.button", text="V Tank").number= pecas.round_1x1_red
        row = layout.row(align=False)
        row.operator("my.button", text="Lever").number= pecas.lever
        row.operator("my.button", text="Snowboard").number= pecas.snowboard_small
        row.operator("my.button", text="Grass").number= pecas.stem_plant
        row = layout.row(align=False)
        row.operator("my.button", text="Red Flower").number= pecas.flower_2_2x2
        row.operator("my.button", text="Green Flower").number= pecas.flower_1_2x2  
        row.operator("my.button", text="Reel").number= pecas.technic_reel_3x2
        row = layout.row(align=False)
        row.operator("my.button", text="Belt Tire").number= pecas.belt_wheel_tire
        row.operator("my.button", text="Small Eye").number= pecas.plate_1x1_eye
        row.operator("my.button", text="Eye").number= pecas.plate_2x2_eye
        row = layout.row(align=False)
        row.operator("my.button", text="Small Tire").number= pecas.tire_30
        row.operator("my.button", text="Big Tire").number= pecas.tire_37 
        row = layout.row(align=False)   
        row.operator("my.button", text="Turntable").number= pecas.turntable_4x4
        row.operator("my.button", text="Wheel").number= pecas.wheel_14_axle

    
#Tools de Step by Step
class tools(bpy.types.Panel):
    bl_label = "Tools"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "constraint"

    def draw(self, context):
        layout = self.layout
        
        
        layout.label("Tools", icon = "SCRIPTWIN")
        row = layout.row(align=False)
        box = row.box()
        box.operator("tools.button", text="5").number=12
        box.operator("tools.button", text="10").number=13
        box.operator("tools.button", text="15").number=14
        col = row.column()
        subrow = col.row()
        subrow.operator("tools.button", text="Location").number=0
        subrow = col.row(align=False) 
        subrow.operator("tools.button", text="Rotation").number=1
        subrow = col.row(align=False)    
        subrow.operator("tools.button", text="Scale").number=2
        subrow = col.row(align=False)  
        subrow.operator("tools.button", text="All Transforms").number=3
        row = layout.row(align=False)
        
        layout.label("SbS Tools", icon = "SCENE")
        row = layout.row(align=False)
        row.operator("tools.button", text="Step").number=4
        row.operator("tools.button", text="Delete Step").number=5
        row = layout.row(align=False)
        row.operator("tools.button", text="Arrow").number=6
        row.operator("tools.button", text="Toon").number=8
        row.operator("tools.button", text="Foto").number=9
        row = layout.row(align=False)
        row.operator("tools.button", text="Hide").number=10
        row.operator("tools.button", text="Unhide").number=11
        layout.label("Settings Tools", icon = "SETTINGS")
        row = layout.row(align=False)
        row.operator("tools.button", text="Reset").number=7
        row.operator("tools.button", text="Set scale and grid").number=15


#Tools de Step by Step Operator
class tools_button(bpy.types.Operator):
    bl_idname = "tools.button"
    bl_label = "Button"
    number = bpy.props.IntProperty()
    
    def execute(self, context):
        if self.number == 0:
            bpy.ops.object.copy_obj_vis_loc()
        elif self.number == 1:
            bpy.ops.object.copy_obj_vis_rot()    
        elif self.number == 2:
            bpy.ops.object.copy_obj_vis_sca()
        elif self.number == 3:
            bpy.ops.object.copy_obj_vis_loc()
            bpy.ops.object.copy_obj_vis_rot()
            bpy.ops.object.copy_obj_vis_sca()
            
        elif self.number == 4:
            
            selection_names = bpy.context.selected_objects

            if selection_names == []:
                bpy.ops.object.select_all(action='SELECT')
    
            else:
                bpy.ops.object.select_all(action='DESELECT')

                bpy.ops.object.select_all(action='SELECT')
            bpy.ops.anim.keyframe_insert_menu(type='LocRotScale')
            bpy.ops.object.select_all(action='DESELECT')  
            
        elif self.number == 5:
            selection_names = bpy.context.selected_objects

            if selection_names == []:
                bpy.ops.object.select_all(action='SELECT')
    
            else:
                bpy.ops.object.select_all(action='DESELECT')

                bpy.ops.object.select_all(action='SELECT')
            bpy.ops.anim.keyframe_delete_v3d()
            bpy.ops.object.select_all(action='DESELECT')  
            
        elif self.number == 6:
            blendfile =  "C:/Users/victor.daga/Documents/Montagens_Lego/cena_pecas/wedo_pieces_v1.7.blend"
                    #"T:/EDITORIAL/02. Ed. Tech/PLUGIN_LEGO/wedo_pieces_TESTE.blend"
                    
            section = "\\Object\\"
            object = "arrow"
            print (object)   
       
            bpy.ops.wm.append(
            filepath=blendfile + section + object, 
            filename=object  ,
            directory=blendfile + section)
            
            blendfile =  "C:/Users/victor.daga/Documents/Montagens_Lego/cena_pecas/wedo_pieces_v1.7.blend"
                    #"T:/EDITORIAL/02. Ed. Tech/PLUGIN_LEGO/wedo_pieces_TESTE.blend"
                    
            section = "\\Object\\"
            object = "empty_arrow"
            print (object)   
       
            bpy.ops.wm.append(
            filepath=blendfile + section + object, 
            filename=object  ,
            directory=blendfile + section)
            
        elif self.number == 7:
            bpy.utils.unregister_module(__name__)

        elif self.number == 8:
            print("----------------------------------------------------------")
            material_list_raw= bpy.data.materials
            material_list=[]
            i=0
            while (i<len(material_list_raw)):
                mat=str(material_list_raw[i])
                mat=mat[23:]
                mat=mat[:-3]
                material_list.append(mat)
                i=i+1
                
            i=0
            while(i<len(material_list)):
                mat_new=material_list[i]

                
                mat=bpy.data.materials[mat_new]
                if mat.use_nodes ==True:
                    nodes = mat.node_tree.nodes
                    for node in nodes:
                        if node.name == 'Mix Shader X':
                            print("OK"+mat_new)
                            bpy.data.materials[mat_new].node_tree.nodes['Mix Shader X'].inputs['Fac'].default_value = 0
                i=i+1

        elif self.number == 9:
            print("----------------------------------------------------------")
            material_list_raw= bpy.data.materials
            material_list=[]
            i=0
            while (i<len(material_list_raw)):
                mat=str(material_list_raw[i])
                mat=mat[23:]
                mat=mat[:-3]
                material_list.append(mat)
                i=i+1
                
            i=0
            while(i<len(material_list)):
                mat_new=material_list[i]

                
                mat=bpy.data.materials[mat_new]
                if mat.use_nodes ==True:
                    nodes = mat.node_tree.nodes
                    for node in nodes:
                        if node.name == 'Mix Shader X':
                            print("OK"+mat_new)
                            bpy.data.materials[mat_new].node_tree.nodes['Mix Shader X'].inputs['Fac'].default_value = 1
                i=i+1
        elif self.number == 10:
            scale = 0
            cont = 0
            obj = bpy.context.selected_objects
            while(cont< len(obj)):
                print(obj[cont])
                bpy.context.scene.objects.active = obj[cont]
                rel_pos = bpy.context.active_object.location.x
                print(rel_pos)
                bpy.context.active_object.location.x = rel_pos + 4
                bpy.context.active_object.scale.x = scale
                bpy.context.active_object.scale.y = scale
                bpy.context.active_object.scale.z = scale
                cont = cont+1

        elif self.number == 11:
            scale = 1
            cont = 0
            obj = bpy.context.selected_objects
            while(cont< len(obj)):
                print(obj[cont])
                bpy.context.scene.objects.active = obj[cont]
                rel_pos = bpy.context.active_object.location.x
                print(rel_pos)
                bpy.context.active_object.location.x = rel_pos - 4
                bpy.context.active_object.scale.x = scale
                bpy.context.active_object.scale.y = scale
                bpy.context.active_object.scale.z = scale
                cont = cont+1

        elif self.number == 12:
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
          
                    area.spaces[0].grid_subdivisions = 5

        elif self.number == 13:
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
          
                    area.spaces[0].grid_subdivisions = 10   

        elif self.number == 14:
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
          
                    area.spaces[0].grid_subdivisions = 15
        elif self.number == 15:
            for area in context.screen.areas:
                if area.type == 'VIEW_3D':
          
                    area.spaces[0].grid_lines= 100
                if area.type == 'VIEW_3D':
          
                    area.spaces[0].grid_scale= 1
                if area.type == 'VIEW_3D':
          
                    area.spaces[0].grid_subdivisions = 10
        return{'FINISHED'} 
    
#   Function Button 
class OBJECT_OT_Button(bpy.types.Operator):
    bl_idname = "my.button"
    bl_label = "Button"
    number = bpy.props.IntProperty()
    
    def execute(self,context):
        
        blendfile =  "C:/Users/victor.daga/Documents/Montagens_Lego/cena_pecas/wedo_pieces_v1.7.blend"

                    #"T:/EDITORIAL/02. Ed. Tech/PLUGIN_LEGO/wedo_pieces_TESTE.blend"
                    
                    
        section = "\\Object\\"
        object = pecas.lista_pecas[self.number]
        print (object)   
       
        bpy.ops.wm.append(
        filepath=blendfile + section + object, 
        filename=object  ,
        directory=blendfile + section)
        #bpy.ops.import_scene.autodesk_3ds(filepath=words[self.number])
        return{'FINISHED'}    
 
#    Registration
bpy.utils.register_module(__name__)







