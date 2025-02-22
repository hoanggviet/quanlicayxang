PGDMP     (            	        |         	   QLCayXang    15.4    15.4 )    '           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            (           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            )           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            *           1262    39225 	   QLCayXang    DATABASE     �   CREATE DATABASE "QLCayXang" WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Vietnamese_Vietnam.1252';
    DROP DATABASE "QLCayXang";
                postgres    false            �            1259    39575    baocao    TABLE     �   CREATE TABLE public.baocao (
    "MaBaoCao" integer NOT NULL,
    "MaCayXang" character varying(50),
    "LoaiBaoCao" character varying(50) NOT NULL,
    "DuLieuBaoCao" text,
    "NgayTaoBaoCao" timestamp without time zone NOT NULL
);
    DROP TABLE public.baocao;
       public         heap    postgres    false            �            1259    39574    baocao_MaBaoCao_seq    SEQUENCE     �   CREATE SEQUENCE public."baocao_MaBaoCao_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 ,   DROP SEQUENCE public."baocao_MaBaoCao_seq";
       public          postgres    false    222            +           0    0    baocao_MaBaoCao_seq    SEQUENCE OWNED BY     O   ALTER SEQUENCE public."baocao_MaBaoCao_seq" OWNED BY public.baocao."MaBaoCao";
          public          postgres    false    221            �            1259    39525    cayxang    TABLE     �  CREATE TABLE public.cayxang (
    "MaCayXang" character varying(50) NOT NULL,
    "TenCayXang" character varying(100) NOT NULL,
    "DiaChi" character varying(255) NOT NULL,
    "ThanhPho" character varying(100) NOT NULL,
    "ViDo" double precision NOT NULL,
    "KinhDo" double precision NOT NULL,
    "TrangThaiHoatDong" boolean,
    "TongNhienLieu" double precision,
    "NhienLieuTieuThu" double precision,
    "DichVu" text
);
    DROP TABLE public.cayxang;
       public         heap    postgres    false            �            1259    39556    danhgia    TABLE     �   CREATE TABLE public.danhgia (
    "MaDanhGia" integer NOT NULL,
    "MaCayXang" character varying(50),
    "MaNguoiDung" integer,
    "DiemDanhGia" integer NOT NULL,
    "BinhLuan" text,
    "NgayDanhGia" timestamp without time zone NOT NULL
);
    DROP TABLE public.danhgia;
       public         heap    postgres    false            �            1259    39555    danhgia_MaDanhGia_seq    SEQUENCE     �   CREATE SEQUENCE public."danhgia_MaDanhGia_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 .   DROP SEQUENCE public."danhgia_MaDanhGia_seq";
       public          postgres    false    220            ,           0    0    danhgia_MaDanhGia_seq    SEQUENCE OWNED BY     S   ALTER SEQUENCE public."danhgia_MaDanhGia_seq" OWNED BY public.danhgia."MaDanhGia";
          public          postgres    false    219            �            1259    39544    gianhienlieu    TABLE     �   CREATE TABLE public.gianhienlieu (
    "MaGia" integer NOT NULL,
    "MaCayXang" character varying(50),
    "LoaiNhienLieu" character varying(50) NOT NULL,
    "GiaBan" double precision NOT NULL,
    "NgayHieuLuc" timestamp without time zone NOT NULL
);
     DROP TABLE public.gianhienlieu;
       public         heap    postgres    false            �            1259    39543    gianhienlieu_MaGia_seq    SEQUENCE     �   CREATE SEQUENCE public."gianhienlieu_MaGia_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 /   DROP SEQUENCE public."gianhienlieu_MaGia_seq";
       public          postgres    false    218            -           0    0    gianhienlieu_MaGia_seq    SEQUENCE OWNED BY     U   ALTER SEQUENCE public."gianhienlieu_MaGia_seq" OWNED BY public.gianhienlieu."MaGia";
          public          postgres    false    217            �            1259    39533 	   nguoidung    TABLE     C  CREATE TABLE public.nguoidung (
    "MaNguoiDung" integer NOT NULL,
    "TenDangNhap" character varying(50) NOT NULL,
    "MatKhau" character varying(255) NOT NULL,
    "VaiTro" character varying(20) NOT NULL,
    "Email" character varying(100) NOT NULL,
    "SoDienThoai" character varying(20),
    "TrangThai" boolean
);
    DROP TABLE public.nguoidung;
       public         heap    postgres    false            �            1259    39532    nguoidung_MaNguoiDung_seq    SEQUENCE     �   CREATE SEQUENCE public."nguoidung_MaNguoiDung_seq"
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;
 2   DROP SEQUENCE public."nguoidung_MaNguoiDung_seq";
       public          postgres    false    216            .           0    0    nguoidung_MaNguoiDung_seq    SEQUENCE OWNED BY     [   ALTER SEQUENCE public."nguoidung_MaNguoiDung_seq" OWNED BY public.nguoidung."MaNguoiDung";
          public          postgres    false    215            {           2604    39578    baocao MaBaoCao    DEFAULT     v   ALTER TABLE ONLY public.baocao ALTER COLUMN "MaBaoCao" SET DEFAULT nextval('public."baocao_MaBaoCao_seq"'::regclass);
 @   ALTER TABLE public.baocao ALTER COLUMN "MaBaoCao" DROP DEFAULT;
       public          postgres    false    222    221    222            z           2604    39559    danhgia MaDanhGia    DEFAULT     z   ALTER TABLE ONLY public.danhgia ALTER COLUMN "MaDanhGia" SET DEFAULT nextval('public."danhgia_MaDanhGia_seq"'::regclass);
 B   ALTER TABLE public.danhgia ALTER COLUMN "MaDanhGia" DROP DEFAULT;
       public          postgres    false    220    219    220            y           2604    39547    gianhienlieu MaGia    DEFAULT     |   ALTER TABLE ONLY public.gianhienlieu ALTER COLUMN "MaGia" SET DEFAULT nextval('public."gianhienlieu_MaGia_seq"'::regclass);
 C   ALTER TABLE public.gianhienlieu ALTER COLUMN "MaGia" DROP DEFAULT;
       public          postgres    false    218    217    218            x           2604    39536    nguoidung MaNguoiDung    DEFAULT     �   ALTER TABLE ONLY public.nguoidung ALTER COLUMN "MaNguoiDung" SET DEFAULT nextval('public."nguoidung_MaNguoiDung_seq"'::regclass);
 F   ALTER TABLE public.nguoidung ALTER COLUMN "MaNguoiDung" DROP DEFAULT;
       public          postgres    false    216    215    216            $          0    39575    baocao 
   TABLE DATA           h   COPY public.baocao ("MaBaoCao", "MaCayXang", "LoaiBaoCao", "DuLieuBaoCao", "NgayTaoBaoCao") FROM stdin;
    public          postgres    false    222   !3                 0    39525    cayxang 
   TABLE DATA           �   COPY public.cayxang ("MaCayXang", "TenCayXang", "DiaChi", "ThanhPho", "ViDo", "KinhDo", "TrangThaiHoatDong", "TongNhienLieu", "NhienLieuTieuThu", "DichVu") FROM stdin;
    public          postgres    false    214   �3       "          0    39556    danhgia 
   TABLE DATA           t   COPY public.danhgia ("MaDanhGia", "MaCayXang", "MaNguoiDung", "DiemDanhGia", "BinhLuan", "NgayDanhGia") FROM stdin;
    public          postgres    false    220   37                  0    39544    gianhienlieu 
   TABLE DATA           f   COPY public.gianhienlieu ("MaGia", "MaCayXang", "LoaiNhienLieu", "GiaBan", "NgayHieuLuc") FROM stdin;
    public          postgres    false    218   P7                 0    39533 	   nguoidung 
   TABLE DATA           {   COPY public.nguoidung ("MaNguoiDung", "TenDangNhap", "MatKhau", "VaiTro", "Email", "SoDienThoai", "TrangThai") FROM stdin;
    public          postgres    false    216   9       /           0    0    baocao_MaBaoCao_seq    SEQUENCE SET     C   SELECT pg_catalog.setval('public."baocao_MaBaoCao_seq"', 1, true);
          public          postgres    false    221            0           0    0    danhgia_MaDanhGia_seq    SEQUENCE SET     F   SELECT pg_catalog.setval('public."danhgia_MaDanhGia_seq"', 1, false);
          public          postgres    false    219            1           0    0    gianhienlieu_MaGia_seq    SEQUENCE SET     G   SELECT pg_catalog.setval('public."gianhienlieu_MaGia_seq"', 1, false);
          public          postgres    false    217            2           0    0    nguoidung_MaNguoiDung_seq    SEQUENCE SET     J   SELECT pg_catalog.setval('public."nguoidung_MaNguoiDung_seq"', 14, true);
          public          postgres    false    215            �           2606    39582    baocao baocao_pkey 
   CONSTRAINT     X   ALTER TABLE ONLY public.baocao
    ADD CONSTRAINT baocao_pkey PRIMARY KEY ("MaBaoCao");
 <   ALTER TABLE ONLY public.baocao DROP CONSTRAINT baocao_pkey;
       public            postgres    false    222            }           2606    39531    cayxang cayxang_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.cayxang
    ADD CONSTRAINT cayxang_pkey PRIMARY KEY ("MaCayXang");
 >   ALTER TABLE ONLY public.cayxang DROP CONSTRAINT cayxang_pkey;
       public            postgres    false    214            �           2606    39563    danhgia danhgia_pkey 
   CONSTRAINT     [   ALTER TABLE ONLY public.danhgia
    ADD CONSTRAINT danhgia_pkey PRIMARY KEY ("MaDanhGia");
 >   ALTER TABLE ONLY public.danhgia DROP CONSTRAINT danhgia_pkey;
       public            postgres    false    220            �           2606    39549    gianhienlieu gianhienlieu_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.gianhienlieu
    ADD CONSTRAINT gianhienlieu_pkey PRIMARY KEY ("MaGia");
 H   ALTER TABLE ONLY public.gianhienlieu DROP CONSTRAINT gianhienlieu_pkey;
       public            postgres    false    218                       2606    39542    nguoidung nguoidung_Email_key 
   CONSTRAINT     ]   ALTER TABLE ONLY public.nguoidung
    ADD CONSTRAINT "nguoidung_Email_key" UNIQUE ("Email");
 I   ALTER TABLE ONLY public.nguoidung DROP CONSTRAINT "nguoidung_Email_key";
       public            postgres    false    216            �           2606    39540 #   nguoidung nguoidung_TenDangNhap_key 
   CONSTRAINT     i   ALTER TABLE ONLY public.nguoidung
    ADD CONSTRAINT "nguoidung_TenDangNhap_key" UNIQUE ("TenDangNhap");
 O   ALTER TABLE ONLY public.nguoidung DROP CONSTRAINT "nguoidung_TenDangNhap_key";
       public            postgres    false    216            �           2606    39538    nguoidung nguoidung_pkey 
   CONSTRAINT     a   ALTER TABLE ONLY public.nguoidung
    ADD CONSTRAINT nguoidung_pkey PRIMARY KEY ("MaNguoiDung");
 B   ALTER TABLE ONLY public.nguoidung DROP CONSTRAINT nguoidung_pkey;
       public            postgres    false    216            �           2606    39583    baocao baocao_MaCayXang_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.baocao
    ADD CONSTRAINT "baocao_MaCayXang_fkey" FOREIGN KEY ("MaCayXang") REFERENCES public.cayxang("MaCayXang") ON DELETE CASCADE;
 H   ALTER TABLE ONLY public.baocao DROP CONSTRAINT "baocao_MaCayXang_fkey";
       public          postgres    false    214    222    3197            �           2606    39564    danhgia danhgia_MaCayXang_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.danhgia
    ADD CONSTRAINT "danhgia_MaCayXang_fkey" FOREIGN KEY ("MaCayXang") REFERENCES public.cayxang("MaCayXang") ON DELETE CASCADE;
 J   ALTER TABLE ONLY public.danhgia DROP CONSTRAINT "danhgia_MaCayXang_fkey";
       public          postgres    false    220    214    3197            �           2606    39569     danhgia danhgia_MaNguoiDung_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.danhgia
    ADD CONSTRAINT "danhgia_MaNguoiDung_fkey" FOREIGN KEY ("MaNguoiDung") REFERENCES public.nguoidung("MaNguoiDung") ON DELETE SET NULL;
 L   ALTER TABLE ONLY public.danhgia DROP CONSTRAINT "danhgia_MaNguoiDung_fkey";
       public          postgres    false    3203    216    220            �           2606    39550 (   gianhienlieu gianhienlieu_MaCayXang_fkey    FK CONSTRAINT     �   ALTER TABLE ONLY public.gianhienlieu
    ADD CONSTRAINT "gianhienlieu_MaCayXang_fkey" FOREIGN KEY ("MaCayXang") REFERENCES public.cayxang("MaCayXang") ON DELETE CASCADE;
 T   ALTER TABLE ONLY public.gianhienlieu DROP CONSTRAINT "gianhienlieu_MaCayXang_fkey";
       public          postgres    false    218    3197    214            $   Z   x�3�t�000��x�k�B^F��Uy
9�w��r:^T�Pq�9/]!���y
X���)Y�X��Y[q��qqq �d#M         �  x��VAk�0>'�B?�K�,��VXZ�-�v1a$��-���<vl�4ƠI)�ne�u��G����=�rl���-G��ާ�}�{��.���b����Ec�L��4��Kuu^��'��ڴ����{�����r��U�h?M���{.L�vY�F$�u��L��<M�����vV�)z۟�nz��u���M�|�V�q��H�y���ON2�:	����Mj�����%�`QK���2I�_"���,�U<��	 cu�s�u6�5��^��{���hbM%u����6����q<K��좮��Mr��
gӪX���7��G�d�?O2�yXlg�UQԼ �B�m�1a>�cF1ӂ�$a�APYH�r8Q���yXA�r�54g>7g&�k�d�1<�cn����K��B��)�4��������4��1�k3����,��Ƶ����Ae�ZP��%�Dg�����~xi�Bg`���A��\�q��>Z:�6�0���UO�)�S9�`&Z�sj��T������l�r��cu����u	`*'��*.�'���Lʱ���=,��u�-k՛¹o��Đ��8�)���T_�p�<c������hM��tX>;8��N�nB�h�J�#p��ԩ�`��
ƍ_�RiFG.Y֘�Mj��t����φ�� ]�G9��X-�+�/و8���`��Cy�#�9A��b���{�##豊�O�E�X/�	��j��k�Ȧ��z���d�1���A10�&��r�VΌ��	��ӵ����ǯ���ux�_���n���������@�ѭ��GՓ���:��nV󲪴tjKm�R��%8���Eq���-ַ8���ɥA�s�J�BC�绒���kiBĵ/Pj	��ٸ(H�S�o� ��u1���Z���h�U����&i %      "      x������ � �          �  x���=NAF��S�A��ZR�D��6BH�q���7!�q�1�,�|�������t��|{�=>�W����	�p_ꮔ�����8!�C�҇�﯏����~z��V��0�.�>��^����(�h�_Nף����/�*=n���4���x� o{�pT|\���;�q3^<���KŇi��z�˸_~��M����H�ͮY���#�Oڄ��-���#��O
��ٚ4
�GJ�x�)l͞��9����STO:E�Y��S���"R<��fa<�n�<r�œNQk(�m?PU���7;�b/����S��'��ެ��^<<r�E�Sܛ5���W�GN�x�)�ͮI��<rJ@�Sқo�O��V<��fk�)Y9%��I��5��-v����}E�SO7�<��t�)         W  x�u�ɒ�J��wQk�2w-2���ʠq7����"�Os��C[�E��8_D�<?T���'|���)ْ&Od]���������$�X!�X�֓��p���נ�٥YB(|I��@%�����\�e�yK sj~i��B+�Z��nc�+�]�u9��<���E�vT����q�O��s����wP|�7H|�qS\�B\���vdl�kz<J�̱	����a��le*�U�A�wPz�4.�q�<��l�N��^;��hR���Jb��3��M̓��M�S�A�
w>�\n ��j,�*U�a@L	��p��S�|b��y��R��2�B?(�A��opX�Z��K��xyQ"��Yrj�����"�pU� fb!���)R�](���d�gBz�22'�IpN��d8�	Te��
g���LyY�S��SeR�ef�[G�~�~>D���o���3�a�_��f�
ϤL�V�U�Lg�R7f�EE���Z��Oa��"�L���as���a!��	Mx5��L�|]����\�b-�G���4��Ek�zD�'B�y���X�7I_�f��l[9:s[���:^Alc��6��i�U&�wd��'Y��d&xE��&qG���At�?�k���9GY��3K<��l��y��,;��s��A?�t'/	AI �=$~�{������7e8׌X�G:�/�K��L��[3n���bx<Z�>�l�w��&���aq��W�푱]��pJ�7��I��9�e[��d���H���[��'8$Z���^��$�ղ �uH�$��#�+Lw����/[-7�7C+��aF'�ֵKPzZ�e�_����%��     