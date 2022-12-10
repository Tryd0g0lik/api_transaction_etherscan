let url = 'https://api-goerli.etherscan.io/api';
let data={
   module:'account',
	action:'txlist',
	address:'0x118ee078c3625144e3a942566fbc84f187f8c8b6',
	startblock:'5',
	endblock:'99999999',
	page:'1',
	offset:'10',
	sort:'asc',
	apikey:'5PNDPQY793WFZ3HMK9TC8MNYXI888P84AK'
];

//$.ajax({
//    url: 'apps_web_scraping/api/files/api_data.json',
//    dataType: 'json',
//    success: function (data) {
//        callBack(data);    // Обрабатываю данные, генерирую таблицу
//    }
//});

//function respone(){
//	console.logo(
//		echo '111111111 TRue'
//	)
//}

let httpRequest = new XMLHttpRequest();
httpRequest.open(
	'GET',
	url + '?'+ data,
	true
);
httpRequest.send(null);

if (httpRequest.status == 200) {
    // великолепно!
}