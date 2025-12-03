import order_request

def test_get_order_by_track():
    track_number = order_request.get_info_by_track()
    assert track_number.status_code == 200