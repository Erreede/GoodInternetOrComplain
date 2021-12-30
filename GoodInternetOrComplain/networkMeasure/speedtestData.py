import speedtest

def performTest():
    try:
        s = speedtest.Speedtest()
        s.get_closest_servers()
        s.download()
        s.upload(pre_allocate=False)
        results = s.results.dict()
        results['png_url'] = s.results.share()
        return results
    except:
        return {'status': "Error"}
