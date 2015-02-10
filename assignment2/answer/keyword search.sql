select docid,sum(mult) as total from(select a.docid,a.term,a.count,b.count,a.count*b.count as mult from frequency a,
(SELECT 'q' as docid, 'washington' as term, 1 as count 
UNION SELECT 'q' as docid, 'taxes' as term, 1 as count UNION SELECT 'q' as docid,'treasury' as term, 1 as count) b where a.term = b.term) group by docid order by total asc