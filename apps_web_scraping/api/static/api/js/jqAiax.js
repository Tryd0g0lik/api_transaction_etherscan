
$(document).ready(function(){
	$('.update').click( function(){
	$.getJSON( "static/api/json/api_data.json",  function( data ) {

	let apiHtml = '';
  let heders = '<li><div class="api__header"> <div>blockNumber</div><div>timeStamp</div><div>hash</div><div>from</div><div>to</div><div>value</div><div>contractAddress</div><div>input</div><div>type</div><div>gas</div><div>gasUsed</div><div>traceId</div><div>isError</div><div>errCode</div></div></li>';

	for (let el = 0; el <= (data.response).length; el++ ){

		apiHtml += '<li><div class="api__header FFF api_value">';
		$.each( data.response[el], function( key, val ) {

			apiHtml += '<div>' + val + '</div>'

		  });
		  apiHtml += ' </div></li>';
      }
		heders = '<ul>' + heders + apiHtml + '</ul>'
		$('.api').html(heders);
		});
		return false

	});

});
