from rediscluster import RedisCluster

url="redis://:R1NFTBWTE1@10.127.91.90:6572/0"

rc = RedisCluster.from_url(url, skip_full_coverage_check=True)

rc.set("foo", "bar")

print(rc.get("foo"))
