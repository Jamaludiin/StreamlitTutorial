import streamlit as st
from io import StringIO


# ---------------------------------------------------------------------------------------------------------
# Declare functions iin here
def clean_txt(user_txt_sidebar):
    user_txt_sidebar = (
        user_txt_sidebar.replace("'", "")
        .replace("-\n", "")
        .replace("\n", "")
        .replace("\n\n", "&&***&&")
        .replace("&&***&&", "\n\n")
        .strip()
    )
    return user_txt_sidebar


# ---------------------------------------------------------------------------------------------------------


# Give title to the app
st.title("This is Streamlit App Title")

# Print text on the app
st.write("My Firts Streamlit App")

# Create sub header
st.subheader("Sub Header")
st.write(
    """Lorem Ipsum is simply dummy text of the **printing** and typesetting industry. *Lorem Ipsum has been the industry's standard dummy text ever* since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."""
)

# Add button to the App
btn_1 = st.button("Submit")

if btn_1:
    st.write("Submitt Button was Pressed! :sunglasses:")
    st.write("*Italic* :sunglasses:")

# Dealing with checkbox
ckb_1 = st.checkbox("I Love Streamlit")

if ckb_1:
    st.write("Everyone Loves!")


# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("CkeckBoxes")
st.write("Select all and Disselect all")

CkeckBox1 = st.checkbox("CkeckBox1", True)
CkeckBox2 = st.checkbox("CkeckBox2")
CkeckBox3 = st.checkbox("CkeckBox3")
CkeckBox4 = st.checkbox("CkeckBox4")
CkeckBox5 = st.checkbox("CkeckBox5")
CkeckBox6 = st.checkbox("CkeckBox6", True)

btn_2 = st.button("Select All")
if btn_2:
    if CkeckBox1 == False:
        st.write("You have not selected CkeckBox 1")

    elif CkeckBox2 == False:
        st.write("You have not selected CkeckBox 2")

    elif CkeckBox3 == False:
        st.write("You have not selected CkeckBox 3")

    elif CkeckBox4 == False:
        st.write("You have not selected CkeckBox 4")

    elif CkeckBox5 == False:
        st.write("You have not selected CkeckBox 5")

    elif CkeckBox6 == False:
        st.write("You have not selected CkeckBox 6")
    else:
        st.write("You have  selected all CkeckBoxes")


# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Radio Buttons")

rdb_1 = st.radio(
    "Select Your Favorite Choice",
    ("Choice 1", "Choice 2", "Choice 3", "Choice 4", "Choice 5"),
)

if rdb_1:
    st.write("You have selected the ", rdb_1, ":heart:")


# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("DropDown Select Box")

country = st.selectbox(
    "Select your Country", ("USA", "UK", "Canada", "NewZealand", "Germany")
)

if country:
    if country == "USA":
        st.write("You have selected the ", country, ":red[**:flag-us:**]")
    elif country == "UK":
        st.write("You have selected the ", country, ":green[***:uk:***]")
    elif country == "Canada":
        st.write("You have selected the ", country, ":blue[**:flag-ca:**]")
    elif country == "NewZealand":
        st.write("You have selected the ", country, ":gray[**:flag-nz:**]")
    elif country == "Germany":
        st.write("You have selected the ", country, ":violet[**:flag-gm:**]")


# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Multi Selector Box")

select_country = st.multiselect(
    "Select your Favorite Countries	:world_map:",
    ({"USA", "UK", "Canada", "NewZealand", "Germany"}),
)

if select_country:
    st.write("You have selected ", select_country, ":earth_americas:")


# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Slider Selector Box")

slided_num = st.slider("This is a single side slider", 1, 100, 75)
st.write("You have selected upto ", slided_num)


slided_range = st.slider("This is a multiple side slider", 1, 100, (25, 75))
if slided_range:
    st.write("You have selected the range between ", slided_range)


# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Input Text Area")

user_input = st.text_input(
    "What is your Favorite Food? :shallow_pan_of_food: :green_salad: :bowl_with_spoon:",
    "Banana",
)

if st.button("Submit Food"):
    st.write(
        "Good to Know that you Like the ",
        user_input,
        ":shallow_pan_of_food: :green_salad: :bowl_with_spoon:",
    )


# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Input Numerica Data")

user_input_num = st.number_input("What is your Favorite Number?", 1, 100, 5)

if st.button("Submit Number"):
    st.write("Good to Know that you Like the ", user_input_num, "Number")


# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Input Text Area")

user_input_txt = st.text_area(
    "Write Your Essay",
    """It is a long established fact that a reader will be distracted by the readable content of a page when looking at its layout. The point of using Lorem Ipsum is that it has a more-or-less normal distribution of letters, as opposed to using 'Content here, content here', making it look like readable English. Many desktop publishing packages and web page editors now use Lorem Ipsum as their default model text, and a search for 'lorem ipsum' will uncover many web sites still in their infancy. Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).""",
    250,
)
if st.button("Submit Text"):
    st.write("**Here is your text**")
    st.write(user_input_txt)


# Streamlit layout structure
# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Streamlit Layouts")


st.sidebar.image("streamlit-mark-color.png", "Streamlit Logo", 150)
st.sidebar.header("Main Menue")
user_txt_sidebar = st.sidebar.text_area("Your Text")
txt_btn = st.sidebar.button("Text Process")
if txt_btn:
    col1, col2 = st.columns(2)
    col1.subheader("UnProcessed Text")
    col1.write(user_txt_sidebar)

    col2.subheader("Processed Text")

    clean = clean_txt(user_txt_sidebar)
    col2.write(clean)


# Streamlit layout structure with exapnder
# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Streamlit Layouts with Expander")

if txt_btn:
    col3, col4 = st.columns(2)

    col3_expander = col3.expander("Expand UnProcessed Text")
    with col3_expander:
        col3_expander.header("Not Processed Text")
        col3_expander.write(user_txt_sidebar)

    col4_expander = col4.expander("Expand Processed Text", True)
    with col4_expander:
        col4_expander.header("Processed Text")
        clean = clean_txt(clean)
        col4_expander.write(clean)


# Streamlit file uppload
# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Streamlit File Uploader")
upload_all_files = st.file_uploader("Upload your Photo")

upload_pdf_2 = st.file_uploader("Upload your PDF", "pdf")

# is optional to write type =
upload_pdf_3 = st.file_uploader(
    "Upload your PNG",
    type="png",
    accept_multiple_files=True,
    help="Multiple file is accepted",
)


byte_data_expander = st.expander("Expand Processed Byte Data", False)
for upload_pdf in upload_pdf_3:
    bytes_data = upload_pdf.read()
    with byte_data_expander:
        byte_data_expander.write(bytes_data)


upload_photo_4 = st.file_uploader(
    "Upload PNG or JPG File",
    type=["png", "jpg"],
    help="Onle file is accepted",
    disabled=False,
    label_visibility="visible",
)
# properties you can set in the uploader
_ = """ 
    type=["png", "jpg"],
    help="Onle file is accepted",
    disabled=True or False,
    label_visibility ("visible", "hidden", or "collapsed")
    accept_multiple_files (bool)
    """
# Convert the uploaded file into byte data
_ = """if upload_photo_4 is not None:
    # To read file as bytes:
    bytes_data = upload_photo_4.getvalue()
    st.write(bytes_data)

    # To convert to a string based IO:
    stringio = StringIO(upload_photo_4.getvalue().decode("utf-8"))
    st.write(stringio)

    # To read file as string:
    string_data = stringio.read()
    st.write(string_data)"""

# Streamlit Camera Input
# ---------------------------------------------------------------------------------------------------------
st.divider()
st.subheader("Streamlit Camera Input")

camera_photo = st.camera_input("Take a Photo")
