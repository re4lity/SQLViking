import trace, sys
from sys import path
path.append("pytds/")
import tds
            
tracer = trace.Trace(count=False, trace=True)

#data = "04011baa00330100e30300120000810500000000000800a764000904d000340565006d00610069006c00000000000800380e63007500730074006f006d00650072004e0075006d00620065007200000000000800a728000904d0003408700061007300730077006f007200640000000000090026020b7100750065007300740069006f006e005f0069006400000000000900a732000904d000340661006e007300770065007200d11d0061647269616e40636f696e616765616e647468696e6773636f2e636f6d1a0100000c00636d4670626d4a7664773d3d02020002004e59d11a00616c656a616e64726140616e67726573656c6c6572732e6e6574ed000000080061485675644756790203000600616e696d616cd11700616c657840706f72746f696d706f727473636f2e6e6574a90000000c0059323974634856305a58493d0202000800436f6c6f7261646fd12000616c6c656e40636f6c6c65637461626c6573666f726c657373696e632e6e65747b0100000800646d6c775a58493d020400080070617373776f7264d11800616c7461676172407261616e616e73746f7265732e6e6574e101000008004d5445784d5445780202000a0043616c69666f726e6961d11700616e6e6574746540616c706861636f676e61632e6e6574f200000008005a326c755a3256790203000300636174d11600616e746f6e40616e746f6e64657369676e732e6e6574d10100000800616d467a63475679020400040061736466d1150061726e6f6c64406372757a736f6e73636f2e6e65748101000008005a6d3976596d46790203000600616e696d616cd11500617368776f72746840617673746f7265732e6e6574bb000000080059574668595746680204000600313233343536d11e006265727472616e64406c61636f726e656461626f6e64616e63652e636f6dac0000000800633268685a4739330203000300636174d11d0062696c6c406175737472616c69616e636f6c6c6563746f72732e6e6574720000000800624739325a513d3d0204000500636f696e73d11800626f62406174656c6965726772617068697175652e636f6d6700000008004d54497a4e4455320201000400626c7565d11b00627261646c65794073636875796c6572696d706f7274732e636f6d2f01000008005a6d78766432567902040006006f70656e7570d11e00627261756e4070726563696f7573636f6c6c65637461626c65732e636f6d7801000008004d5863795a544e6c0202000800436f6c6f7261646fd11b0062726f776e407374796c6973686465736b6465636f72732e6e6574440100000c006347467a63336377636d513d0201000800736b7920626c7565d1220063616c616768616e406175737472616c69616e676f6c646e6574776f726b2e6e65744d0100000c005a6e4a705a57356b63773d3d0204000600313233343536d11d006361737369647940636c6f766572636f6c6c656374696f6e732e6e6574bd0000000c00633356775a584a745957343d0203000300636174d11900636174686572696e654070657469746d6574616c732e6e65743a01000008005a3239765a32786c0201000400626c7565d11e0063657276616e74657340636c6173736963676f6c6469646561732e6e657453010000080063323176613256350203000300646f67d11c006368616e646c6572406d656e72757372657461696c6572732e636f6d5b0100000c005a476c6e6158526862413d3d0203000600616e696d616cd12300636c656e6168616e406175737472616c69616e636f6c6c65637461626c65732e6e6574d70100000c005a474675615756736247553d0203000300646f67d11d006372616d6572406372616d65727370657a69616c697474656e2e636f6d4f010000080061474679624756350204000500636f696e73d1150064616e40676f6c646964656173636f72702e6e6574bf0100000c005932396a59574e766247453d0201000400626c7565d1160064616e69656c406c796f6e636f696e6167652e6e6574fa0000000800595842776247553d0201000500677265656ed11b0064616e69656c406d6574616c736173736f6369736369652e636f6d000100000c0061577876646d56356233557a0203000300646f67d118006465766f6e40756b636f6c6c65637461626c65732e636f6dc90000000c005a6d397664474a686247773d0203000300646f67d12b00646f6e6e65726d6579657240626176617269616e636f6c6c65637461626c6573696d706f7274732e6e65749f0100000c006232356c624739325a513d3d0203000600616e696d616cd12200646f70726563696f7573717565406d6574616c7363616e616c70657469742e636f6d9601000008005a4746736247467a0201000400626c7565d12400646f726f746879406f6e6c696e657072656d69756d6372656174696f6e73636f2e6e65746b0100000800634739335a58493d02020005005465786173d11600656440626765636f6c6c65637461626c65732e6e657425010000080059323974634746780201000400626c7565d11d006564756172646f40656e61636f6469737472696275746f72732e636f6dd80000000c006332396a593246794d513d3d0201000a006c6967687420626c7565d11b0066657565724066657565726f6e6c696e6573746f7265732e6e6574bb0100000c00596e5669596d786c63773d3d0201000800736b7920626c7565d11b006672616e636f40667261756461636f6c6c657a696f6e652e636f6dd901000008005957356e5a5777780201000400626c7565d117006672616e6b656e406672616e6b656e676f6c642e6e6574110100000800636d39696233513d0203000300646f67d11b0066726472697175654070726563696f75736361726176792e6e6574d10000000c006347467a63336476636d51780204000400676f6c64d11c0067616f406b696e676b6f6e67636f6c6c65637461626c65732e6e6574d30000000c0061577876646d5635623355780201000800736b7920626c7565d11e0067656f72674073616c7a62757267636f6c6c65637461626c65732e636f6d7e0100000c0059334a6c59585270646d553d0202000700466c6f72696461d1180067696f76616e6e6940726f76656c6c69676f6c642e636f6d1601000008005a335670644746790204000500636f696e73d11b0067726168616d40646f776e756e646572636f696e6167652e6e65744301000008005958567a64476c750202000700466c6f72696461d1170068616e6e61406d6974766572676e67656e636f2e636f6ddd01000008006332467462586b3d0203000300636174d1180068656c656e40676f6c6462796d61696c636f756b2e6e6574f00000000800633235766233423502020008004d6973736f757269d11200686f6c7a407669646173706f72742e6e65742a01000008005a3239735a413d3d0201000500677265656ed11800686f727374406e6174726c6963686d6574616c732e636f6ddf0000000c00596d467a5a574a686247777802020004004f68696fd118006a616d6573406c616e646f66636f696e73696e632e6e6574830000000800614739775a513d3d02020002004e59d11b006a616e6540766f6c766f6d6f64656c7265706c696361732e6e6574900000000800625739306147567902020005005465786173d121006a65616e407175626563686f6d6573686f7070696e676e6574776f726b2e636f6de9000000080062334a68626d646c0202000a0043616c69666f726e6961d117006a656666406d7573636c65636f696e73696e632e6e6574970000000c00624756306257567062673d3d020400040061736466d121006a657272794063616d627269646765636f6c6c65637461626c6573636f2e636f6dad0000000c00615735305a584a755a58513d0204000600313233343536d117006a6572727940676f6174676f6c6473746f72652e6e6574700000000c006347467a63336476636d513d0203000300646f67d114006a6573757340636166696d706f7274732e6e65745801000008006248566a61336b3d0203000300646f67d11d006a696c6c406261616e6570726563696f7573696d706f7274732e6e6574790000000c0063484a70626d4e6c63334d3d0203000300636174d11b006a756c696540636f696e733467726f776e757073636f6d2e636f6dcd0000000c0062576c6a6147466c62413d3d02020005005465786173d11e006a756c696540636f72706f72617465676f6c646964656173636f2e636f6d410100000800595752746157343d0204000600717765727479d116006a756c696540676f6c646465706f74696e632e636f6daf0000000c0064326868644756325a58493d0204000600313233343536d11a006a756c69654070726563696f75736d6574616c73636f2e636f6d810000000800633356746257567902020005005465786173d118006a75726940676f6c6434616c6c61676573636f6d2e6e65746a01000008006147396a61325635020400040061736466d119006b616c6c654073756f6d696e656e636f696e6167652e636f6d4e0100000c00626d6c75644756755a47383d02020008004e657720596f726bd11a006b6172696e406b6f6d6d697373696f6e6d6574616c732e6e6574690100000c0059323979646d56306447553d0201000400626c7565d11c006b61727474756e656e40636f696e736f6666696e6c616e642e6e6574ba000000080062574630636d6c3402020002005458d118006b61746540626c617565727365656d6574616c732e6e6574800000000c0061577876646d56356233553d0202000700466c6f72696461d119006b6569746840616d65726963616e62616e6b696e632e636f6da8000000080062573975613256350201000800736b7920626c7565d11d006b656c76696e407072656d69756d636c617373696373696e632e636f6d9d0000000c0064484a3163335275627a453d0204000600313233343536d11c006b6c6165626f65406e6f72776179676f6c6462796d61696c2e6e65742b01000008005932397662413d3d02020008004e657720596f726bd11d006b6f736b6974616c6f406f756c75746f79737570706c6965732e6e65743701000008006257567962476c750202000800436f6c6f7261646fd119006b75676572407361726469737472696275746f72732e6e65746401000008005a5735305a58493d0203000300646f67d124006c617572656e6365406d61727365696c6c6570726563696f75736d6574616c732e6e65745e010000080063334270636d6c300203000300646f67d120006c65736c6965406d6574616c73636f696e636c617373696373696e632e636f6dc60000000c00634739725a57317662673d3d0203000300636174d119006c65736c696540737570657273696c766572696e632e636f6dc70100000800596d466965513d3d02020008004e657720596f726bd125006c696e636f6c6e40726f79616c63616e616469616e636f6c6c65637461626c65732e6e657404010000080063326c73646d56790204000500636f696e73d11b006d6172696140636c61737369636c6567656e6473696e632e636f6da80100000c0062576c6a636d397a62325a300201000800736b7920626c7565d117006d61726b406c61726f6368656c6c65676f6c642e6e6574770000000c004d54497a4e4455324e7a673d02020004004f68696fd11a006d61727461406d61727461737265706c69636173636f2e636f6d1e01000008005a474672623352680201000300726564d120006d6172746861407363616e64696e617669616e676f6c6469646561732e636f6dc00100000800624739326157356e0203000600616e696d616cd122006d617274696e654064616564616c757364657369676e73696d706f7274732e636f6dab000000080059584e6b5a673d3d0204000600313233343536d116006d61727940626f61726473636f696e73636f2e636f6ddb0000000c0061577876646d56356233556802020002004e59d11c006d617474406575726f73686f7070696e676368616e6e656c2e6e65748d0000000c006247397661326c755a773d3d0201000a006c6967687420626c7565d11b006d617572697a696f406c6f7264696e65636f696e6167652e6e657482010000080063327868655756790204000400676f6c64d11a006d636b656e6e6140617369616e7472656173757265732e6e65745c0100000c0064476831626d526c63673d3d02020008004e657720596f726bd120006d63726f794065787472656d656465736b6465636f726174696f6e732e636f6d9c0100000c006447567a6448526c6333513d0203000300646f67d116006d656c4064657268756e64696d706f7274732e6e6574330100000c0063324e766233526c63673d3d0204000600313233343536d119006d69636861656c40766974616368726f6d65696e632e6e6574b500000008006347467a63773d3d0202000200464cd125006d696775656c406f6e6c696e6570726563696f7573636f6c6c65637461626c65732e6e6574cc0000000800614756736347316c0202000700466c6f72696461d117006d6f7279406f73616b61636f696e616765636f2e6e6574b100000008005932686c5a584e6c02020005005465786173d11a006f6861726140616e6e61736465636f726174696f6e732e636f6d14010000080063475668626e56300203000300646f67d11d0070616c6c65406865696e747a65636f6c6c65637461626c65732e636f6de30000000c006358646c636e52354d513d3d020400080070617373776f7264d1160070616f6c6f40616d696361636f696e73636f2e636f6df90000000c006447567a64476c755a773d3d0204000500636f696e73d11800706173696c76657240726f79616c6562656c67652e636f6d7d0100000c006358646c636e52354d513d3d0201000400626c7565d11a007061756c407265696d73636f6c6c65637461626c65732e636f6d610100000800596d46755a476c300201000400626c7565d11e007066616c7a6865696d40746f6d737370657a69616c697474656e2e6e657403010000080059324675595752680203000300646f67d1210072656e617465406d6573736e657273686f7070696e676e6574776f726b2e636f6df70000000c006258567a644746755a773d3d0202000a0043616c69666f726e6961d125007269746140737475747467617274636f6c6c65637461626c6565786368616e67652e636f6d9901000008005a334a6c5a57343d0201000300726564d11600726f6240736176656c657968656e72696f742e6e65749200000008006147467763486b3d0202000700466c6f72696461d11b00726f6472696775657a406c6973626f61636f696e6167652e6e6574710100000c00596d5675616d46746157343d0203000300646f67d11a00726f656c40696265726961676f6c64696d706f7274732e636f6de40100000c0062476c6e614852756157356e0201000400626c7565d11e00726f6c616e644070726563696f75736d6574616c737765726b652e636f6dc40100000c00625746346432567362413d3d0203000300636174d12100726f736140636f696e726d696e746469737472696275746f7273696e632e636f6de60100000c00636d56745a5731695a58493d0203000300636174d1200073616c6c794064616e69736877686f6c6573616c65696d706f7274732e636f6d910000000c005a6d397664474a686247773d02020002004e59d1190073616d40746563686e69637373746f726573696e632e636f6da1000000080059574a6a4d54497a02020008004e657720596f726bd11f0073656d656e6f76406b72656d6c696e636f6c6c65637461626c65732e636f6de00100000800626d39755a513d3d0203000600616e696d616cd11f007368696d616d75726140746f6b796f636f6c6c65637461626c65732e636f6d8e010000080064326c7a5a4739740203000300636174d11600736b7940686176656c7a6279737a656b636f2e636f6d7d000000080063326c755a32786c0202000a0043616c69666f726e6961d12000736d69746840646f75626c656465636b6572676f6c6473746f7265732e636f6de90100000c006247563062575670626a453d0203000300646f67d12000736f6d6d657240636f72726964616d6574616c737265706c696361732e6e6574ca01000008005a475634644756790203000300646f67d11700737465766540647261676f6e636f696e6167652e636f6d9400000008006358646c636e52350203000300636174d11a0073746576654070726563696f7573636c6173736963732e6e65743f0100000c0063335268636e52795a57733d0202000800436f6c6f7261646fd1210073746576654077657374636f617374636f6c6c65637461626c6573636f2e6e6574db01000008004e5455314e54553102040007006c65746d65696ed11d00737565407369676e616c636f6c6c65637469626c65736c74642e6e6574e701000008006233426c626e56770202000a0043616c69666f726e6961d11d00737565407468657368617270676f6c6477617265686f7573652e6e6574c20100000c006347467a63336476636d51680203000300636174d12500737573616e4070726563696f7573676f6c646469737472696275746f72736c74642e636f6d7c0000000c006333567563326870626d553d0202000a0043616c69666f726e6961d118007376656e407761726275726765786368616e67652e636f6dcb010000080061326c30644756750201000a006c6967687420626c7565d11700746f6e79406b656c6c7973676f6c6473686f702e6e6574f00100000c0063335268636e6468636e4d3d0201000800736b7920626c7565d1280076616c6172696540636f6c6c65637461626c6570726563696f757364657369676e73636f2e636f6def0000000c00616d5675626d6c6d5a58493d0204000500636f696e73d11f0076616c61726965407072656d69756d636f6c6c65637461626c65732e636f6def01000008006248566a61336b780201000400626c7565d11200766579406865726b6b75676f6c642e6e6574a700000008005a484a685a3239750201000400626c7565d11b0076696f6c6574614066756e676f6c646964656173636f6d2e636f6dce01000008006333526c624778680203000300646f67d1170077616c657340676f6c64666f7268696d636f6d2e6e6574650100000c00595735306147397565513d3d02040006006f70656e7570d11f0077616c6b657240617369616e73686f7070696e676e6574776f726b2e636f6dce00000008006332566a636d56300203000300646f67d1160077656e64794068616e646a69676f6c64636f2e636f6da60000000800614756736247383d0201000800736b7920626c7565d1200077696c6c69616d4074656b6e69636f6c6c65637461626c6573696e632e6e657448010000080064326c75626d56790201000300726564d11d0077696e674070726563696f75736372656174696f6e736c74642e6e6574400100000c0062574630636d6c3449513d3d020400080070617373776f7264d12500796f7368694063616e616469616e676f6c6465786368616e67656e6574776f726b2e636f6dca0000000c00596d786861474a735957673d02040007006c65746d65696ed115007975406d6963726f73696c766572696e632e636f6dc8010000080063484a70626d4e6c02020008004e657720596f726bfd1000c1007a00000000000000".decode("hex")
#data = "0401034200340100aa2a03b13b000001106901530051004c002000530065007200760065007200200062006c006f0063006b00650064002000610063006300650073007300200074006f002000700072006f00630065006400750072006500200027007300790073002e00780070005f0063006d0064007300680065006c006c00270020006f006600200063006f006d0070006f006e0065006e00740020002700780070005f0063006d0064007300680065006c006c0027002000620065006300610075007300650020007400680069007300200063006f006d0070006f006e0065006e00740020006900730020007400750072006e006500640020006f00660066002000610073002000700061007200740020006f0066002000740068006500200073006500630075007200690074007900200063006f006e00660069006700750072006100740069006f006e00200066006f0072002000740068006900730020007300650072007600650072002e00200041002000730079007300740065006d002000610064006d0069006e006900730074007200610074006f0072002000630061006e00200065006e00610062006c0065002000740068006500200075007300650020006f00660020002700780070005f0063006d0064007300680065006c006c00270020006200790020007500730069006e0067002000730070005f0063006f006e006600690067007500720065002e00200046006f00720020006d006f0072006500200069006e0066006f0072006d006100740069006f006e002000610062006f0075007400200065006e00610062006c0069006e00670020002700780070005f0063006d0064007300680065006c006c0027002c002000730065006100720063006800200066006f00720020002700780070005f0063006d0064007300680065006c006c002700200069006e002000530051004c002000530065007200760065007200200042006f006f006b00730020004f006e006c0069006e0065002e001a570049004e002d00490033004d00300051004d00480030004800340056005c00530051004c0045005800500052004500530053000b780070005f0063006d0064007300680065006c006c0001000000fe0200e0000000000000000000".decode('hex')
#data = "0401009800330100aa8000d000000001101f0049006e00760061006c006900640020006f0062006a0065006300740020006e0061006d00650020002700620075006c006c00730068006900740027002e001a570049004e002d00490033004d00300051004d00480030004800340056005c00530051004c0045005800500052004500530053000001000000fd0200fd000000000000000000".decode('hex')
data = "04011baa00330100e30300120000810500000000000800a764000904d000340565006d00610069006c00000000000800380e63007500730074006f006d00650072004e0075006d00620065007200000000000800a728000904d0003408700061007300730077006f007200640000000000090026020b7100750065007300740069006f006e005f0069006400000000000900a732000904d000340661006e007300770065007200d11d0061647269616e40636f696e616765616e647468696e6773636f2e636f6d1a0100000c00636d4670626d4a7664773d3d02020002004e59d11a00616c656a616e64726140616e67726573656c6c6572732e6e6574ed000000080061485675644756790203000600616e696d616cd11700616c657840706f72746f696d706f727473636f2e6e6574a90000000c0059323974634856305a58493d0202000800436f6c6f7261646fd12000616c6c656e40636f6c6c65637461626c6573666f726c657373696e632e6e65747b0100000800646d6c775a58493d020400080070617373776f7264d11800616c7461676172407261616e616e73746f7265732e6e6574e101000008004d5445784d5445780202000a0043616c69666f726e6961d11700616e6e6574746540616c706861636f676e61632e6e6574f200000008005a326c755a3256790203000300636174d11600616e746f6e40616e746f6e64657369676e732e6e6574d10100000800616d467a63475679020400040061736466d1150061726e6f6c64406372757a736f6e73636f2e6e65748101000008005a6d3976596d46790203000600616e696d616cd11500617368776f72746840617673746f7265732e6e6574bb000000080059574668595746680204000600313233343536d11e006265727472616e64406c61636f726e656461626f6e64616e63652e636f6dac0000000800633268685a4739330203000300636174d11d0062696c6c406175737472616c69616e636f6c6c6563746f72732e6e6574720000000800624739325a513d3d0204000500636f696e73d11800626f62406174656c6965726772617068697175652e636f6d6700000008004d54497a4e4455320201000400626c7565d11b00627261646c65794073636875796c6572696d706f7274732e636f6d2f01000008005a6d78766432567902040006006f70656e7570d11e00627261756e4070726563696f7573636f6c6c65637461626c65732e636f6d7801000008004d5863795a544e6c0202000800436f6c6f7261646fd11b0062726f776e407374796c6973686465736b6465636f72732e6e6574440100000c006347467a63336377636d513d0201000800736b7920626c7565d1220063616c616768616e406175737472616c69616e676f6c646e6574776f726b2e6e65744d0100000c005a6e4a705a57356b63773d3d0204000600313233343536d11d006361737369647940636c6f766572636f6c6c656374696f6e732e6e6574bd0000000c00633356775a584a745957343d0203000300636174d11900636174686572696e654070657469746d6574616c732e6e65743a01000008005a3239765a32786c0201000400626c7565d11e0063657276616e74657340636c6173736963676f6c6469646561732e6e657453010000080063323176613256350203000300646f67d11c006368616e646c6572406d656e72757372657461696c6572732e636f6d5b0100000c005a476c6e6158526862413d3d0203000600616e696d616cd12300636c656e6168616e406175737472616c69616e636f6c6c65637461626c65732e6e6574d70100000c005a474675615756736247553d0203000300646f67d11d006372616d6572406372616d65727370657a69616c697474656e2e636f6d4f010000080061474679624756350204000500636f696e73d1150064616e40676f6c646964656173636f72702e6e6574bf0100000c005932396a59574e766247453d0201000400626c7565d1160064616e69656c406c796f6e636f696e6167652e6e6574fa0000000800595842776247553d0201000500677265656ed11b0064616e69656c406d6574616c736173736f6369736369652e636f6d000100000c0061577876646d56356233557a0203000300646f67d118006465766f6e40756b636f6c6c65637461626c65732e636f6dc90000000c005a6d397664474a686247773d0203000300646f67d12b00646f6e6e65726d6579657240626176617269616e636f6c6c65637461626c6573696d706f7274732e6e65749f0100000c006232356c624739325a513d3d0203000600616e696d616cd12200646f70726563696f7573717565406d6574616c7363616e616c70657469742e636f6d9601000008005a4746736247467a0201000400626c7565d12400646f726f746879406f6e6c696e657072656d69756d6372656174696f6e73636f2e6e65746b0100000800634739335a58493d02020005005465786173d11600656440626765636f6c6c65637461626c65732e6e657425010000080059323974634746780201000400626c7565d11d006564756172646f40656e61636f6469737472696275746f72732e636f6dd80000000c006332396a593246794d513d3d0201000a006c6967687420626c7565d11b0066657565724066657565726f6e6c696e6573746f7265732e6e6574bb0100000c00596e5669596d786c63773d3d0201000800736b7920626c7565d11b006672616e636f40667261756461636f6c6c657a696f6e652e636f6dd901000008005957356e5a5777780201000400626c7565d117006672616e6b656e406672616e6b656e676f6c642e6e6574110100000800636d39696233513d0203000300646f67d11b0066726472697175654070726563696f75736361726176792e6e6574d10000000c006347467a63336476636d51780204000400676f6c64d11c0067616f406b696e676b6f6e67636f6c6c65637461626c65732e6e6574d30000000c0061577876646d5635623355780201000800736b7920626c7565d11e0067656f72674073616c7a62757267636f6c6c65637461626c65732e636f6d7e0100000c0059334a6c59585270646d553d0202000700466c6f72696461d1180067696f76616e6e6940726f76656c6c69676f6c642e636f6d1601000008005a335670644746790204000500636f696e73d11b0067726168616d40646f776e756e646572636f696e6167652e6e65744301000008005958567a64476c750202000700466c6f72696461d1170068616e6e61406d6974766572676e67656e636f2e636f6ddd01000008006332467462586b3d0203000300636174d1180068656c656e40676f6c6462796d61696c636f756b2e6e6574f00000000800633235766233423502020008004d6973736f757269d11200686f6c7a407669646173706f72742e6e65742a01000008005a3239735a413d3d0201000500677265656ed11800686f727374406e6174726c6963686d6574616c732e636f6ddf0000000c00596d467a5a574a686247777802020004004f68696fd118006a616d6573406c616e646f66636f696e73696e632e6e6574830000000800614739775a513d3d02020002004e59d11b006a616e6540766f6c766f6d6f64656c7265706c696361732e6e6574900000000800625739306147567902020005005465786173d121006a65616e407175626563686f6d6573686f7070696e676e6574776f726b2e636f6de9000000080062334a68626d646c0202000a0043616c69666f726e6961d117006a656666406d7573636c65636f696e73696e632e6e6574970000000c00624756306257567062673d3d020400040061736466d121006a657272794063616d627269646765636f6c6c65637461626c6573636f2e636f6dad0000000c00615735305a584a755a58513d0204000600313233343536d117006a6572727940676f6174676f6c6473746f72652e6e6574700000000c006347467a63336476636d513d0203000300646f67d114006a6573757340636166696d706f7274732e6e65745801000008006248566a61336b3d0203000300646f67d11d006a696c6c406261616e6570726563696f7573696d706f7274732e6e6574790000000c0063484a70626d4e6c63334d3d0203000300636174d11b006a756c696540636f696e733467726f776e757073636f6d2e636f6dcd0000000c0062576c6a6147466c62413d3d02020005005465786173d11e006a756c696540636f72706f72617465676f6c646964656173636f2e636f6d410100000800595752746157343d0204000600717765727479d116006a756c696540676f6c646465706f74696e632e636f6daf0000000c0064326868644756325a58493d0204000600313233343536d11a006a756c69654070726563696f75736d6574616c73636f2e636f6d810000000800633356746257567902020005005465786173d118006a75726940676f6c6434616c6c61676573636f6d2e6e65746a01000008006147396a61325635020400040061736466d119006b616c6c654073756f6d696e656e636f696e6167652e636f6d4e0100000c00626d6c75644756755a47383d02020008004e657720596f726bd11a006b6172696e406b6f6d6d697373696f6e6d6574616c732e6e6574690100000c0059323979646d56306447553d0201000400626c7565d11c006b61727474756e656e40636f696e736f6666696e6c616e642e6e6574ba000000080062574630636d6c3402020002005458d118006b61746540626c617565727365656d6574616c732e6e6574800000000c0061577876646d56356233553d0202000700466c6f72696461d119006b6569746840616d65726963616e62616e6b696e632e636f6da8000000080062573975613256350201000800736b7920626c7565d11d006b656c76696e407072656d69756d636c617373696373696e632e636f6d9d0000000c0064484a3163335275627a453d0204000600313233343536d11c006b6c6165626f65406e6f72776179676f6c6462796d61696c2e6e65742b01000008005932397662413d3d02020008004e657720596f726bd11d006b6f736b6974616c6f406f756c75746f79737570706c6965732e6e65743701000008006257567962476c750202000800436f6c6f7261646fd119006b75676572407361726469737472696275746f72732e6e65746401000008005a5735305a58493d0203000300646f67d124006c617572656e6365406d61727365696c6c6570726563696f75736d6574616c732e6e65745e010000080063334270636d6c300203000300646f67d120006c65736c6965406d6574616c73636f696e636c617373696373696e632e636f6dc60000000c00634739725a57317662673d3d0203000300636174d119006c65736c696540737570657273696c766572696e632e636f6dc70100000800596d466965513d3d02020008004e657720596f726bd125006c696e636f6c6e40726f79616c63616e616469616e636f6c6c65637461626c65732e6e657404010000080063326c73646d56790204000500636f696e73d11b006d6172696140636c61737369636c6567656e6473696e632e636f6da80100000c0062576c6a636d397a62325a300201000800736b7920626c7565d117006d61726b406c61726f6368656c6c65676f6c642e6e6574770000000c004d54497a4e4455324e7a673d02020004004f68696fd11a006d61727461406d61727461737265706c69636173636f2e636f6d1e01000008005a474672623352680201000300726564d120006d6172746861407363616e64696e617669616e676f6c6469646561732e636f6dc00100000800624739326157356e0203000600616e696d616cd122006d617274696e654064616564616c757364657369676e73696d706f7274732e636f6dab000000080059584e6b5a673d3d0204000600313233343536d116006d61727940626f61726473636f696e73636f2e636f6ddb0000000c0061577876646d56356233556802020002004e59d11c006d617474406575726f73686f7070696e676368616e6e656c2e6e65748d0000000c006247397661326c755a773d3d0201000a006c6967687420626c7565d11b006d617572697a696f406c6f7264696e65636f696e6167652e6e657482010000080063327868655756790204000400676f6c64d11a006d636b656e6e6140617369616e7472656173757265732e6e65745c0100000c0064476831626d526c63673d3d02020008004e657720596f726bd120006d63726f794065787472656d656465736b6465636f726174696f6e732e636f6d9c0100000c006447567a6448526c6333513d0203000300646f67d116006d656c4064657268756e64696d706f7274732e6e6574330100000c0063324e766233526c63673d3d0204000600313233343536d119006d69636861656c40766974616368726f6d65696e632e6e6574b500000008006347467a63773d3d0202000200464cd125006d696775656c406f6e6c696e6570726563696f7573636f6c6c65637461626c65732e6e6574cc0000000800614756736347316c0202000700466c6f72696461d117006d6f7279406f73616b61636f696e616765636f2e6e6574b100000008005932686c5a584e6c02020005005465786173d11a006f6861726140616e6e61736465636f726174696f6e732e636f6d14010000080063475668626e56300203000300646f67d11d0070616c6c65406865696e747a65636f6c6c65637461626c65732e636f6de30000000c006358646c636e52354d513d3d020400080070617373776f7264d1160070616f6c6f40616d696361636f696e73636f2e636f6df90000000c006447567a64476c755a773d3d0204000500636f696e73d11800706173696c76657240726f79616c6562656c67652e636f6d7d0100000c006358646c636e52354d513d3d0201000400626c7565d11a007061756c407265696d73636f6c6c65637461626c65732e636f6d610100000800596d46755a476c300201000400626c7565d11e007066616c7a6865696d40746f6d737370657a69616c697474656e2e6e657403010000080059324675595752680203000300646f67d1210072656e617465406d6573736e657273686f7070696e676e6574776f726b2e636f6df70000000c006258567a644746755a773d3d0202000a0043616c69666f726e6961d125007269746140737475747467617274636f6c6c65637461626c6565786368616e67652e636f6d9901000008005a334a6c5a57343d0201000300726564d11600726f6240736176656c657968656e72696f742e6e65749200000008006147467763486b3d0202000700466c6f72696461d11b00726f6472696775657a406c6973626f61636f696e6167652e6e6574710100000c00596d5675616d46746157343d0203000300646f67d11a00726f656c40696265726961676f6c64696d706f7274732e636f6de40100000c0062476c6e614852756157356e0201000400626c7565d11e00726f6c616e644070726563696f75736d6574616c737765726b652e636f6dc40100000c00625746346432567362413d3d0203000300636174d12100726f736140636f696e726d696e746469737472696275746f7273696e632e636f6de60100000c00636d56745a5731695a58493d0203000300636174d1200073616c6c794064616e69736877686f6c6573616c65696d706f7274732e636f6d910000000c005a6d397664474a686247773d02020002004e59d1190073616d40746563686e69637373746f726573696e632e636f6da1000000080059574a6a4d54497a02020008004e657720596f726bd11f0073656d656e6f76406b72656d6c696e636f6c6c65637461626c65732e636f6de00100000800626d39755a513d3d0203000600616e696d616cd11f007368696d616d75726140746f6b796f636f6c6c65637461626c65732e636f6d8e010000080064326c7a5a4739740203000300636174d11600736b7940686176656c7a6279737a656b636f2e636f6d7d000000080063326c755a32786c0202000a0043616c69666f726e6961d12000736d69746840646f75626c656465636b6572676f6c6473746f7265732e636f6de90100000c006247563062575670626a453d0203000300646f67d12000736f6d6d657240636f72726964616d6574616c737265706c696361732e6e6574ca01000008005a475634644756790203000300646f67d11700737465766540647261676f6e636f696e6167652e636f6d9400000008006358646c636e52350203000300636174d11a0073746576654070726563696f7573636c6173736963732e6e65743f0100000c0063335268636e52795a57733d0202000800436f6c6f7261646fd1210073746576654077657374636f617374636f6c6c65637461626c6573636f2e6e6574db01000008004e5455314e54553102040007006c65746d65696ed11d00737565407369676e616c636f6c6c65637469626c65736c74642e6e6574e701000008006233426c626e56770202000a0043616c69666f726e6961d11d00737565407468657368617270676f6c6477617265686f7573652e6e6574c20100000c006347467a63336476636d51680203000300636174d12500737573616e4070726563696f7573676f6c646469737472696275746f72736c74642e636f6d7c0000000c006333567563326870626d553d0202000a0043616c69666f726e6961d118007376656e407761726275726765786368616e67652e636f6dcb010000080061326c30644756750201000a006c6967687420626c7565d11700746f6e79406b656c6c7973676f6c6473686f702e6e6574f00100000c0063335268636e6468636e4d3d0201000800736b7920626c7565d1280076616c6172696540636f6c6c65637461626c6570726563696f757364657369676e73636f2e636f6def0000000c00616d5675626d6c6d5a58493d0204000500636f696e73d11f0076616c61726965407072656d69756d636f6c6c65637461626c65732e636f6def01000008006248566a61336b780201000400626c7565d11200766579406865726b6b75676f6c642e6e6574a700000008005a484a685a3239750201000400626c7565d11b0076696f6c6574614066756e676f6c646964656173636f6d2e636f6dce01000008006333526c624778680203000300646f67d1170077616c657340676f6c64666f7268696d636f6d2e6e6574650100000c00595735306147397565513d3d02040006006f70656e7570d11f0077616c6b657240617369616e73686f7070696e676e6574776f726b2e636f6dce00000008006332566a636d56300203000300646f67d1160077656e64794068616e646a69676f6c64636f2e636f6da60000000800614756736247383d0201000800736b7920626c7565d1200077696c6c69616d4074656b6e69636f6c6c65637461626c6573696e632e6e657448010000080064326c75626d56790201000300726564d11d0077696e674070726563696f75736372656174696f6e736c74642e6e6574400100000c0062574630636d6c3449513d3d020400080070617373776f7264d12500796f7368694063616e616469616e676f6c6465786368616e67656e6574776f726b2e636f6dca0000000c00596d786861474a735957673d02040007006c65746d65696ed115007975406d6963726f73696c766572696e632e636f6dc8010000080063484a70626d4e6c02020008004e657720596f726bfd1000c1007a00000000000000".decode('hex')

tdssock = tds._TdsSocket(data)
try:
	while True:
		tdssock._main_session.find_result_or_done()
except:
	#print sys.exc_info()
	pass

try:
	print tdssock._main_session.messages[0]['message']
except:
	a='no messages'
for a in tdssock._main_session.results:
	print a

#tracer.runfunc(tdssock._main_session.find_result_or_done)
#res = tracer.results()
#res.write_results(coverdir='traceoutput')
