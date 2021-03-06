__author__ = 'July'
# https://leetcode.com/problems/design-in-memory-file-system/#/description
#Design an in-memory file system to simulate the following functions:
#
# ls: Given a path in string format. If it is a file path,
# return a list that only contains this file's name.
# If it is a directory path, return the list of file and directory names in this directory.
# Your output (file and directory names together) should in lexicographic order.
#
# mkdir: Given a directory path that does not exist,
# you should make a new directory according to the path.
# If the middle directories in the path don't exist either,
# you should create them as well. This function has void return type.
#
# addContentToFile: Given a file path and file content in string format.
# If the file doesn't exist, you need to create that file containing given content.
# If the file already exists, you need to append given content to original content.
# This function has void return type.
#
# readContentFromFile: Given a file path, return its content in string format.
#
# Example:
# Input:
# ["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
# [[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]
# Output:
# [null,[],null,null,["a"],"hello"]
# Explanation:
# filesystem
# Note:
# You can assume all file or directory paths are absolute paths
# which begin with / and do not end with / except that the path is just "/".
# You can assume that all operations will be passed valid parameters
# and users will not attempt to retrieve file content or list a directory or file
# that does not exist.
# You can assume that all directory names and file names only contain lower-case letters,
# and same names won't exist in the same directory.
# Hide Company Tags Baidu
# Hide Tags Design
# Hide Similar Problems (H) LRU Cache (H) LFU Cache
java = '''
public class FileSystem {
     class File{
        boolean isFile = false;
        Map<String, File> children = new HashMap<>();
        String content ="";
    }
    File root = null;

    public FileSystem() {
        root = new File();
    }

    public List<String> ls(String path) {
        String[] dirs = path.split("/");
        File node = root;
        List<String> res = new ArrayList<>();
        String name = "";
        for (String dir : dirs) {
            if (dir.length() == 0) continue;
            if (!node.children.containsKey(dir)){
                return res;
            }
            node = node.children.get(dir);
            name = dir;
        }
        if(node.isFile) {
            res.add(name);
        }else {
            for (String key : node.children.keySet()){
                res.add(key);
            }
        }
        Collections.sort(res);
        return res;
    }

    public void mkdir(String path) {
        String[] dirs = path.split("/");
        File node = root;
        for ( String dir : dirs) {
            if(dir.length() == 0) {
                continue;
            }
            if (!node.children.containsKey(dir)){
                File file = new File();
                node.children.put(dir, file);
            }
            node = node.children.get(dir);
        }
    }

    public void addContentToFile(String filePath, String content) {
        String[] dirs = filePath.split("/");
        File node = root;
        for (String dir: dirs) {
            if(dir.length() == 0) continue;
            if(!node.children.containsKey(dir)){
                File file = new File();
                node.children.put(dir,file);
            }
            node = node.children.get(dir);
        }
        node.isFile = true;
        node.content += content;
    }

    public String readContentFromFile(String filePath) {
        String[] dirs = filePath.split("/");
        File node = root;
        for (String dir : dirs) {
            if (dir.length() == 0)continue;
            if(!node.children.containsKey(dir)){
                File file = new File();
                node.children.put(dir, file);
            }
            node = node.children.get(dir);
        }
        return node.content;
    }
}

/**
 * Your FileSystem object will be instantiated and called as such:
 * FileSystem obj = new FileSystem();
 * List<String> param_1 = obj.ls(path);
 * obj.mkdir(path);
 * obj.addContentToFile(filePath,content);
 * String param_4 = obj.readContentFromFile(filePath);
 */

 '''