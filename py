==> ajusta_planilhas_ead_com_cpf.py <==
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import sys
import re

planilhas = {
    u'CÂMPUS ÁGUAS LINDAS.csv': 3647,
    u'CÂMPUS ANÁPOLIS.csv': 699,

==> ajusta_planilhas_ead_sem_cpf.py <==
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import sys
import re

planilhas = {
    u'CÂMPUS ÁGUAS LINDAS.csv': 3647,
    u'CÂMPUS ANÁPOLIS.csv': 699,

==> ajusta_planilhas_presencial_com_cpf.py <==
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import sys
import re

planilhas = {
    u'CÂMPUS ÁGUAS LINDAS.csv': 3647,
    u'CÂMPUS ANÁPOLIS.csv': 699,

==> ajusta_planilhas_presencial_sem_cpf.py <==
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import sys
import re

planilhas = {
    u'CÂMPUS ÁGUAS LINDAS.csv': 3647,
    u'CÂMPUS ANÁPOLIS.csv': 699,

==> ajusta_planilhas.py <==
#!/usr/bin/python3
# -*- coding: utf-8 -*-

from os import path
import sys

planilhas = {
    u'CÂMPUS ÁGUAS LINDAS.csv': 3647,
    u'CÂMPUS ANÁPOLIS.csv': 699,
    u'CÂMPUS APARECIDA DE GOIÂNIA.csv': 210,

==> doc <==

==> gerar_planilha_completa.sh <==
#!/bin/bash
set -e
# este script gera a planilha csv com todos os campus
arquivo="planilha_$(date +%Y%m%d_%H%M%S).csv"
echo "NO_ALUNO;NU_CPF;CO_CURSO;DT_DATA_INICIO;DT_DATA_FIM_PREVISTO;NO_CICLO_MATRICULA;CO_TIPO_OFERTA_CURSO;CO_POLO;NO_STATUS_MATRICULA" > $arquivo
for i in ./C*.csv; do
    sed -n -e "2,$ p" "$i" >> $arquivo
done
exit 0

==> LICENSE <==
                    GNU GENERAL PUBLIC LICENSE
                       Version 3, 29 June 2007

 Copyright (C) 2007 Free Software Foundation, Inc. <http://fsf.org/>
 Everyone is permitted to copy and distribute verbatim copies
 of this license document, but changing it is not allowed.

                            Preamble

  The GNU General Public License is a free, copyleft license for

==> README.md <==
# sistec-download-manual
SISTEC-DOWNLOAD-MANUAL: filtro de dados coletados do SISTEC (http://sistec.mec.gov.br)

## Baixe manualmente as planilhas do SISTEC, procurando os alunos com "_" (underline)

## crie as seguintes pastas:
* `mkdir ead\com_cpf`
* `mkdir ead\sem_cpf`
* `mkdir presencial\com_cpf`
* `mkdir presencial\sem_cpf`

==> sistec_cod_cursos <==

==> sistec_cod_cursos.7z <==
7z��' W���9+      #       `-�� !�Ąm��C��դ��@9jB�u���u e��?�P-x�l��ׁ>/�εd������wX��L´�%M0F ��_���MkY./�{�7��7�rGP��7'VFw��#6*氂���O�{��}2��U��� =���wm�ܜ�6����28IJ��9��Q=�i�ǅ'pa���{�ƴf؜�:lk��1Z�g_�a���j��҄�+��n�&�e�8���7F��rЎ����b"I̯b8�6G���w�_�l$�o�'�=O!'�͌�mGS�_�f��&��M��/{��`G��<?�<�d�c1&�|�ËU[��{7p%�LP������ZE��d����#��V"�E�f��%��P�E�r#*�BsE�)F+�&G�؋�l�����&?�}_�(�M+�ͯ"N��͊n Rf~�h�2�&����L�r��^�u�C���rg_���/ H��!��Ф�c�N�|�/���H���0%�	 �>�v&�	��Wk�m���I�LN�Lw�k�|��M��y��E����~=�e%��	pG<�t� %ԃ�@f^)�	����(���_�����<raxKz��>��I!��NjF�>�el�X�������ۻmpy&b �+��0<���7G��eB+�֪�#$3���&�$��mu->�����b��B��R	20��'l]���~1麈�
&Qjc�!�e�(���)v7b��U�i+a"�Kt0�4��TY#��\z_����faM_U�k׆<L׀�螥=q�Ȳη��|	�@�dE&4��n��c�g����ӣ3�"-�7���{�o4)�ʫ����1�UL���z|�PK)$�ͳ��f�(��w��b	_�!a��
�:.�aWv����a�s������yewB"�+�YY<ӗUEus�zG���,�x]�<��f/)_��}�d��VR^p�{���9�?��(8 ;�5�E+J�dJK�<��U�`��4�O�bJ]a^�k�ٶ�T[���ES��"}��J
ssn5U��,�׼غkX�2������Ap׷��A��,��]{#Uq��D�u���=I�~��E����{Qu���fQ��m��D����7%�0��9��H�I��f	�9�RP뢏's�ʹ��z� �W��"�[DǶ��S���s���UG�'�7�"����._WI`�A�?����|��"���	s�=e��$�	�d���q���=�		���&&Jl��'�
r�&���;l���D��?�e#u�@�^0�_2d�3��f�|���#�r�e�qS��9�	$D}�أaތ���t6�^V��	;oO�<�8�Vjy`�@:�����u�IϷ���U�a�	.p/H����(K��(�a��	m^�6�Ӫ�IV����$+��lc︈��sR=<��g�[O�SÖ��I!;�ACI���e�󌎧-�2COz�Q^�۱��!0A���f!�����,J���`��"%�\��r@|�g)K�5��k`ۨ5��g��tI�go���[��R3'��	b7�
�T>��1�7/(��k=.��'��u�{�:�·_�iUd����=Lk$�q{u�{��ds4�'�G�Ę ����W��G�8ߞיX_����q��P���Q�B���,6[o�!�UG�_�kl��֚��%n]�nurJђ��Q�2l�a�bx泅�_Q��NC���nf�r�/�lD��tY5d.G%�.Z㹺>�6UN�%��𶹎*/��
J���"��ۤB��a������XZ���"	��~�� �<o X��	im�[�����<������a����[���N^���^D[��6�jA��c�ݕ��� ��W��
4�kޝ�'�H���֑��nT������޵��� ��ĸ�f�eubY$K�ھbCK���4�S�)p�]
T�nK)���]�7n��@�O	q�S��Zii�EFd�=e&� 肰�R<�h�X>��P1%����L�\s�1�iNP�Exݒ��$ɼ�{uQ��vi�?T7Q)I�F����3����(��65Tt�-_��@��]4}2�	�_�↬�V���#�(�������Fk<R��|$l	a���y齿��@��UH���G�������Px�8KK��3��P��R#`]YR�_�(Q\����]F!f� ۛ�Q�lc�f��$3`CЈ\��1�eU�Y��!���j����P�Y�ZJu���8��V����g��([p��H�thk��1Ho�A���	'mi�AS�N�ɊIlg.ϖ����� ^��ύQ�}�lU�#����_m�^EXf��d��7D��p�3��\��t���pc�~5RͲ�8��[#nc9�'�:�s�A5����σ�D9����@��^�ab�9��ub�o)��%{��d�W����hز�ր�,i["ل�'���N_� �{���Z�\O���y�c�yH(Rs=w�	�C�_֝�N#���8��'6+ t	
�	�j�ũ'ޤ�2��kY�g(j(MW �K?j@�K�-����i�uE���0�m�d�2l�1�������E��f��Tu1(�6*j(`�A�j�0�:*ʣ%�: ;8$"��Ƶ>_c��c�2�c�x�c��g�`X�} K��)͘x�a����,���~(+�d�j��>k$HUV$�ז�8�H��Йeױ����d;��Z}:,���%�"����[�ELB����w�u���J�E�%d�<�����C�"�9��WH���]��?�$̎C�所sq�x�R�r����@uz=T��!�lE�UM�x��w�3	M�|4�nF�^��(pW�ͮ�ˋŌ�w�����kB����Q�Zm)Ȁ��	��y�e�O)� |�bI-9*�� +�{A_��(#w�6�ڕ�j�Ոb��C�RuM#�mtЌ"��NyG�4�8ۊ+!��K�/��kgN'ϡ_�FT�UU�>��(0�Ȣ��g�������|�&+:֥L���x���6;�o
