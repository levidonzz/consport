import python_avatars as pa


def generate_avatar(user):
    my_avatar = pa.Avatar(
        style=pa.AvatarStyle.CIRCLE,
        background_color=pa.BackgroundColor.BLACK,
        top=pa.HairType.STRAIGHT_2,
        eyebrows=pa.EyebrowType.DEFAULT_NATURAL,
        eyes=pa.EyeType.DEFAULT,
        nose=pa.NoseType.DEFAULT,
        mouth=pa.MouthType.EATING,
        facial_hair=pa.FacialHairType.NONE,
        # You can use hex colors on any color attribute...
        skin_color="#00FFFF",
        # Or you can use the colors provided by the library
        hair_color=pa.HairColor.BLACK,
        accessory=pa.AccessoryType.NONE,
        clothing=pa.ClothingType.HOODIE,
        clothing_color=pa.ClothingColor.HEATHER
    )

    # Save to a file
    return my_avatar.render()