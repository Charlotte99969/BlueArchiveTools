import json
import os

import cv2

from ImageManager import ImageManager

class Skill:
    def __init__(self, ex_skill_level, normal_skill_level, passive_skill_level, sub_skill_level):
        self.ex_skill_level = ex_skill_level
        self.normal_skill_level = normal_skill_level
        self.passive_skill_level = passive_skill_level
        self.sub_skill_level = sub_skill_level

class Equipment:
    def __init__(self, attack_item_level, defense_item_level, support_item_level, unique_item_level):
        self.attack_item_level = attack_item_level
        self.defense_item_level = defense_item_level
        self.support_item_level = support_item_level
        self.unique_item_level = unique_item_level

class Character:
    def __init__(self, id, name, chinese_name):
        self.id = id
        self.name = name
        self.chinese_name = chinese_name

        self.unlocked = False
        self.level = 1
        self.bond_level = 1
        self.quantity = 1
        self.unique_equipment = 0
        self.unique_equipment_level = 0
        self.skill = Skill(1, 1, 1, 1)
        self.equipment = Equipment(1, 1, 1, 0)

    def to_array(self):
        return {
            "id": self.id,
            "name": self.name,
            "current": {
                "level": self.level,
                "ue_level": self.unique_equipment_level,
                "bond": self.bond_level,
                "ex": self.skill.ex_skill_level,
                "basic": self.skill.normal_skill_level,
                "passive": self.skill.passive_skill_level,
                "sub": self.skill.sub_skill_level,
                "gear1": self.equipment.attack_item_level,
                "gear2": self.equipment.defense_item_level,
                "gear3": self.equipment.support_item_level,
                "star": self.quantity,
                "ue": self.unique_equipment
            },
            "target": {
                "level": "",
                "ue_level": "",
                "bond": "",
                "ex": "",
                "basic": "",
                "passive": "",
                "sub": "",
                "gear1": "",
                "gear2": "",
                "gear3": "",
                "star": "",
                "ue": ""
            },
            "eleph": {
                "owned": "0",
                "unlocked": True,
                "cost": "1",
                "purchasable": "20",
                "farm_nodes": "0",
                "node_refresh": False,
                "use_eligma": False,
                "use_shop": False
            },
            "enabled": self.unlocked
        }

characters_data = {
    'Aru': Character(10000, 'Aru', '亞瑠'),
    'Eimi': Character(10001, 'Eimi', '英美'),
    'Haruna': Character(10002, 'Haruna', '羽留奈'),
    'Hifumi': Character(10003, 'Hifumi', '日步美'),
    'Hina': Character(10004, 'Hina', '陽奈'),
    'Hoshino': Character(10005, 'Hoshino', '星野'),
    'Iori': Character(10006, 'Iori', '伊織'),
    'Maki': Character(10007, 'Maki', '真紀'),
    'Neru': Character(10008, 'Neru', '寧瑠'),
    'Izumi': Character(10009, 'Izumi', '泉'),
    'Shiroko': Character(10010, 'Shiroko', '白子'),
    'Shun': Character(10011, 'Shun', '旬'),
    'Sumire': Character(10012, 'Sumire', '堇'),
    'Tsurugi': Character(10013, 'Tsurugi', '弦生'),
    'Akane': Character(13000, 'Akane', '朱音'),
    'Chise': Character(13001, 'Chise', '知世'),
    'Akari': Character(13002, 'Akari', '亞伽里'),
    'Hasumi': Character(13003, 'Hasumi', '蓮實'),
    'Nonomi': Character(13004, 'Nonomi', '野乃美'),
    'Kayoko': Character(13005, 'Kayoko', '佳世子'),
    'Mutsuki': Character(13006, 'Mutsuki', '無月'),
    'Junko': Character(13007, 'Junko', '淳子'),
    'Serika': Character(13008, 'Serika', '茜香'),
    'Tsubaki': Character(13009, 'Tsubaki', '椿'),
    'Yuuka': Character(13010, 'Yuuka', '優香'),
    'Haruka': Character(16000, 'Haruka', '遙香'),
    'Asuna': Character(16001, 'Asuna', '明日奈'),
    'Kotori': Character(16002, 'Kotori', '亞都梨'),
    'Suzumi': Character(16003, 'Suzumi', '鈴美'),
    'Pina': Character(16004, 'Pina', '菲娜'),
    'Hibiki': Character(20000, 'Hibiki', '響'),
    'Karin': Character(20001, 'Karin', '花凛'),
    'Saya': Character(20002, 'Saya', '沙耶'),
    'Airi': Character(23000, 'Airi', '愛莉'),
    'Fuuka': Character(23001, 'Fuuka', '風華'),
    'Hanae': Character(23002, 'Hanae', '花繪'),
    'Hare': Character(23003, 'Hare', '晴'),
    'Utaha': Character(23004, 'Utaha', '詠葉'),
    'Ayane': Character(23005, 'Ayane', '綾音'),
    'Chinatsu': Character(26000, 'Chinatsu', '千夏'),
    'Kotama': Character(26001, 'Kotama', '小玉'),
    'Juri': Character(26002, 'Juri', '茱莉'),
    'Serina': Character(26003, 'Serina', '芹奈'),
    'Shimiko': Character(26004, 'Shimiko', '志美子'),
    'Yoshimi': Character(26005, 'Yoshimi', '喜美'),
    'Mashiro': Character(20003, 'Mashiro', '麻白'),
    'Izuna': Character(10014, 'Izuna', '伊樹菜'),
    'Shizuko': Character(23006, 'Shizuko', '靜子'),
    'Aris': Character(10015, 'Aris', '愛麗絲'),
    'Midori': Character(10016, 'Midori', '綠'),
    'Momoi': Character(13011, 'Momoi', '桃井'),
    'Cherino': Character(10017, 'Cherino', '潔莉諾'),
    'Nodoka': Character(26006, 'Nodoka', '和香'),
    'Yuzu': Character(10018, 'Yuzu', '柚子'),
    'Azusa': Character(10019, 'Azusa', '梓'),
    'Hanako': Character(23007, 'Hanako', '花子'),
    'Koharu': Character(10020, 'Koharu', '小春'),
    'Azusa_Swimsuit': Character(10021, 'Azusa (Swimsuit)', '梓(泳裝)'),
    'Tsurugi_Swimsuit': Character(16005, 'Tsurugi (Swimsuit)', '弦生(泳裝)'),
    'Mashiro_Swimsuit': Character(20004, 'Mashiro (Swimsuit)', '麻白(泳裝)'),
    'Hifumi_Swimsuit': Character(20005, 'Hifumi (Swimsuit)', '日步美(泳裝)'),
    'Hina_Swimsuit': Character(10022, 'Hina (Swimsuit)', '陽奈(泳裝)'),
    'Iori_Swimsuit': Character(10023, 'Iori (Swimsuit)', '伊織(泳裝)'),
    'Izumi_Swimsuit': Character(16006, 'Izumi (Swimsuit)', '泉(泳裝)'),
    'Shiroko_Cycling': Character(10024, 'Shiroko (Cycling)', '白子(單車)'),
    'Shun_Small': Character(10025, 'Shun (Small)', '旬(幼女)'),
    'Kirino': Character(13012, 'Kirino', '桐乃'),
    'Saya_Casual': Character(20006, 'Saya (Casual)', '沙耶(私服)'),
    'Neru_Bunny': Character(10026, 'Neru (Bunny)', '寧瑠(兔女郎)'),
    'Karin_Bunny': Character(10027, 'Karin (Bunny)', '花凛(兔女郎)'),
    'Asuna_Bunny': Character(10028, 'Asuna (Bunny)', '明日奈(兔女郎)'),
    'Natsu': Character(10029, 'Natsu', '夏'),
    'Mari': Character(23008, 'Mari', '瑪麗'),
    'HatsuneMiku': Character(20007, 'Hatsune Miku', '初音未來'),
    'Ako': Character(20008, 'Ako', '亞子'),
    'Chinatsu_HotSpring': Character(10030, 'Chinatsu (HotSpring)', '千夏(溫泉)'),
    'Tomoe': Character(16007, 'Tomoe', '智惠'),
    'Cherino_HotSpring': Character(20009, 'Cherino (HotSpring)', '潔莉諾(溫泉)'),
    'Nodoka_HotSpring': Character(20010, 'Nodoka (HotSpring)', '和香(溫泉)'),
    'Aru_NewYear': Character(10031, 'Aru (NewYear)', '亞瑠(正月)'),
    'Mutsuki_NewYear': Character(10032, 'Mutsuki (NewYear)', '無月(正月)'),
    'Serika_NewYear': Character(20011, 'Serika (NewYear)', '茜香(正月)'),
    'Wakamo': Character(10033, 'Wakamo', '若藻'),
    'Fubuki': Character(16008, 'Fubuki', '吹雪'),
    'Sena': Character(20012, 'Sena', '瀨奈'),
    'Chihiro': Character(20013, 'Chihiro', '千尋'),
    'Mimori': Character(10034, 'Mimori', '三森'),
    'Ui': Character(10035, 'Ui', '憂'),
    'Hinata': Character(10036, 'Hinata', '日向'),
    'Marina': Character(10037, 'Marina', '瑪麗娜'),
    'Miyako': Character(10038, 'Miyako', '都子'),
    'Saki': Character(20014, 'Saki', '咲希'),
    'Miyu': Character(10039, 'Miyu', '美優'),
    'Michiru': Character(16009, 'Michiru', '三千留'),
    'Kaede': Character(20015, 'Kaede', '楓'),
    'Iroha': Character(20016, 'Iroha', '伊呂波'),
    'Tsukuyo': Character(10040, 'Tsukuyo', '月夜'),
    'Misaki': Character(10041, 'Misaki', '美咲'),
    'Hiyori': Character(20017, 'Hiyori', '日和'),
    'Atsuko': Character(10042, 'Atsuko', '敦子'),
    'Wakamo_Swimsuit': Character(10043, 'Wakamo (Swimsuit)', '若藻(泳裝)'),
    'Nonomi_Swimsuit': Character(10044, 'Nonomi (Swimsuit)', '野乃美(泳裝)'),
    'Ayane_Swimsuit': Character(26007, 'Ayane (Swimsuit)', '綾音(泳裝)'),
    'Hoshino_Swimsuit': Character(10045, 'Hoshino (Swimsuit)', '星野(泳裝)'),
    'Shizuko_Swimsuit': Character(26008, 'Shizuko (Swimsuit)', '靜子(泳裝)'),
    'Izuna_Swimsuit': Character(10046, 'Izuna (Swimsuit)', '伊樹菜(泳裝)'),
    'Chise_Swimsuit': Character(10047, 'Chise (Swimsuit)', '知世(泳裝)'),
    'Saori': Character(10048, 'Saori', '沙織'),
    'Kazusa': Character(10049, 'Kazusa', '千紗'),
    'Moe': Character(20018, 'Moe', '萌'),
    'Kokona': Character(10050, 'Kokona', '心菜'),
    'Utaha_CheerSquad': Character(10051, 'Utaha (Cheer Squad)', '詠葉(應援團)'),
    'Noa': Character(10052, 'Noa', '乃愛'),
    'Hibiki_CheerSquad': Character(16010, 'Hibiki (Cheer Squad)', '響(應援團)'),
    'Akane_Bunny': Character(20019, 'Akane (Bunny)', '朱音(兔女郎)'),
    'Yuuka_Track': Character(10053, 'Yuuka (Track)', '優香(體育服)'),
    'Mari_Track': Character(10054, 'Mari (Track)', '瑪麗(體育服)'),
    'Hasumi_Track': Character(16011, 'Hasumi (Track)', '蓮實(體育服)'),
    'Himari': Character(20020, 'Himari', '陽葵'),
    'Shigure': Character(10055, 'Shigure', '時雨'),
    'Serina_Christmas': Character(10056, 'Serina (Christmas)', '芹奈(聖誕節)'),
    'Hanae_Christmas': Character(20021, 'Hanae (Christmas)', '花繪(聖誕節)'),
    'Haruna_NewYear': Character(10057, 'Haruna (NewYear)', '羽留奈(正月)'),
    'Junko_NewYear': Character(16012, 'Junko (NewYear)', '淳子(正月)'),
    'Fuuka_NewYear': Character(20022, 'Fuuka (NewYear)', '風華(正月)'),
    'Mine': Character(10058, 'Mine', '美禰'),
    'Mika': Character(10059, 'Mika', '彌香'),
    'Megu': Character(10060, 'Megu', '惠'),
    'Kanna': Character(20023, 'Kanna', '環奈'),
    'Sakurako': Character(10061, 'Sakurako', '櫻子'),
    'Toki': Character(10062, 'Toki', '季'),
    'Nagisa': Character(20024, 'Nagisa', '渚'),
    'Koyuki': Character(10063, 'Koyuki', '小雪'),
    'Kayoko_NewYear': Character(10064, 'Kayoko (NewYear)', '佳世子(正月)'),
    'Haruka_NewYear': Character(20025, 'Haruka (NewYear)', '遙香(正月)'),
    'Kaho': Character(10065, 'Kaho', '佳穗'),
    'Aris_Maid': Character(10066, 'Aris (Maid)', '愛麗絲(女僕)'),
    'Toki_Bunny': Character(10067, 'Toki (Bunny)', '季(兔女郎)'),
    'Yuzu_Maid': Character(26009, 'Yuzu (Maid)', '柚子(女僕)'),
    'Reisa': Character(10068, 'Reisa', '澪紗'),
    'Rumi': Character(10069, 'Rumi', '瑠美'),
    'Mina': Character(10070, 'Mina', '美奈'),
    'Minori': Character(20026, 'Minori', '實里'),
    'Miyako_Swimsuit': Character(10071, 'Miyako (Swimsuit)', '都子(泳裝)'),
    'Saki_Swimsuit': Character(10072, 'Saki (Swimsuit)', '咲希(泳裝)'),
    'Miyu_Swimsuit': Character(26010, 'Miyu (Swimsuit)', '美優(泳裝)'),
    'Shiroko_Swimsuit': Character(20027, 'Shiroko (Swimsuit)', '白子(泳裝)'),
    'Ui_Swimsuit': Character(10073, 'Ui (Swimsuit)', '憂(泳裝)'),
    'Koharu_Swimsuit': Character(16013, 'Koharu (Swimsuit)', '小春(泳裝)'),
    'Hinata_Swimsuit': Character(20028, 'Hinata (Swimsuit)', '日向(泳裝)'),
    'Hanako_Swimsuit': Character(10074, 'Hanako (Swimsuit)', '花子(泳裝)'),
    'Mimori_Swimsuit': Character(20029, 'Mimori (Swimsuit)', '三森(泳裝)'),
    'Meru': Character(10075, 'Meru', '梅露'),
    'Momiji': Character(13013, 'Momiji', '紅葉'),
    'Kotori_CheerSquad': Character(10076, 'Kotori (Cheer Squad)', '亞都梨(応援団)'),
    'Haruna_Track': Character(20030, 'Haruna (Track)', '羽留奈(体操服)'),
    'Ichika': Character(10077, 'Ichika', 'イチカ'),
    'Kasumi': Character(10078, 'Kasumi', 'カスミ'),
}

class CharacterManager:
    def __init__(self):
        self.characters_directory = "characters"  # 保存影格的目錄
        self.total_progress = 0
        self.current_progress = 0
        self.processing_completed = False

    def export_characters_data(self):
        # 讀取所有圖片文件
        image_files = [os.path.join(self.characters_directory, filename) for filename in os.listdir(self.characters_directory)]
        self.total_progress = len(image_files)  # 圖片文件總數

        for image_path in image_files:
            image = cv2.imread(image_path)
            character_name, file_extension = os.path.splitext(os.path.basename(image_path))

            characters_data[character_name].unlocked = True

            character_level = ImageManager.extract_character_level(image)
            characters_data[character_name].level = character_level

            character_quantity = ImageManager.extract_character_quantity(image)
            characters_data[character_name].quantity = character_quantity

            character_unique_equipment = ImageManager.extract_character_unique_equipment(image)
            characters_data[character_name].unique_equipment = character_unique_equipment

            character_unique_equipment_level = ImageManager.extract_character_unique_equipment_level(image)
            characters_data[character_name].unique_equipment_level = character_unique_equipment_level

            character_bond_level = ImageManager.extract_character_bond_level(image)
            characters_data[character_name].bond_level = character_bond_level

            character_ex_skill_level = ImageManager.extract_character_ex_skill_level(image)
            characters_data[character_name].skill.ex_skill_level = character_ex_skill_level

            character_normal_skill_level = ImageManager.extract_character_normal_skill_level(image)
            characters_data[character_name].skill.normal_skill_level = character_normal_skill_level

            character_passive_skill_level = ImageManager.extract_character_passive_skill_level(image)
            characters_data[character_name].skill.passive_skill_level = character_passive_skill_level

            character_sub_skill_level = ImageManager.extract_character_sub_skill_level(image)
            characters_data[character_name].skill.sub_skill_level = character_sub_skill_level

            character_attack_item_level = ImageManager.extract_character_attack_item_level(image)
            characters_data[character_name].equipment.attack_item_level = character_attack_item_level

            character_defense_item_level = ImageManager.extract_character_defense_item_level(image)
            characters_data[character_name].equipment.defense_item_level = character_defense_item_level

            character_support_item_level = ImageManager.extract_character_support_item_level(image)
            characters_data[character_name].equipment.support_item_level = character_support_item_level

            self.current_progress += 1
            # if self.current_progress > 10:
            #     break
            print(characters_data[character_name].name)
            print(characters_data[character_name].to_array()['current'])

        self.format_to_file()
        self.processing_completed = True

    def format_to_file(self):
        justin163_data = {
            "exportVersion": 2,
            "characters": [],
            "disabled_characters": [],
            "owned_materials": {},
            "groups": {
                "Binah": [],
                "Chesed": [],
                "Hod": [],
                "ShiroKuro": [],
                "Perorodzilla": [],
                "Goz": [],
                "Hieronymous": [],
                "Kaiten": []
            },
            "language": "Tw",
            "level_cap": 87,
            "server": "Global",
            "site_version": "1.4.0",
            "character_order": []
        }
        for name, character in characters_data.items():
            if character.unlocked:
                justin163_data['characters'].append(character.to_array())

        # 将字典转换为 JSON 字符串
        characters_json = json.dumps(justin163_data)

        # 指定要保存 JSON 的文件路径
        json_file_path = 'characters.json'

        # 将 JSON 字符串写入文件
        with open(json_file_path, 'w') as json_file:
            json_file.write(characters_json)
