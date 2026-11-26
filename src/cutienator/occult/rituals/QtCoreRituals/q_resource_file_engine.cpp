//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qresource_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qresource_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QFlags>
#include <QtCore/QIODeviceBase>
#include <optional>
#include <QtCore/QFile>
#include <QtCore/QDateTime>
#include <QtCore/QString>
#include <QtCore/QDirListing>
#include <QtCore/QList>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qresource.h>
#include <QtCore/private/qresource_p.h>
#include <QtCore/private/qresource_iterator_p.h>
#include <QtCore/qset.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qdebug.h>
#include <QtCore/qlocale.h>
#include <QtCore/qglobal.h>
#include <QtCore/qlist.h>
#include <QtCore/qdatetime.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qstringlist.h>
#include <QtCore/qvarlengtharray.h>
#include <QtCore/qendian.h>
#include <QtCore/qshareddata.h>
#include <qplatformdefs.h>
#include <QtCore/qendian.h>
#include <QtCore/private/qabstractfileengine_p.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtCore/private/qnumeric_p.h>
#include <QtCore/private/qsimd_p.h>
#include <QtCore/private/qtools_p.h>
#include <QtCore/private/qsystemerror_p.h>
#ifndef QT_NO_COMPRESS
#  include <zconf.h>
#  include <zlib.h>
#endif
#if QT_CONFIG(zstd)
#  include <zstd.h>
#endif
#if defined(Q_OS_UNIX) && !defined(Q_OS_INTEGRITY)
#  include <sys/mman.h>
#  ifdef Q_OS_LINUX
#  elif defined(Q_OS_DARWIN)
#    include <mach/mach.h>
#    include <mach/vm_map.h>
#  endif
#endif
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qresource.cpp, line 81, as local:qresource.cpp:QStringSplitter
namespace {
class QStringSplitter
{
public:
    explicit QStringSplitter(QStringView sv)
        : m_data(sv.data()), m_len(sv.size())
    {
    }

    inline bool hasNext()
    {
        while (m_pos < m_len && m_data[m_pos] == m_splitChar)
            ++m_pos;
        return m_pos < m_len;
    }

    inline QStringView next()
    {
        const qsizetype start = m_pos;
        while (m_pos < m_len && m_data[m_pos] != m_splitChar)
            ++m_pos;
        return QStringView(m_data + start, m_pos - start);
    }

    const QChar *m_data;
    qsizetype m_len;
    qsizetype m_pos = 0;
    QChar m_splitChar = u'/';
};
}  // namespace

//  from src/corelib/io/qresource.cpp, line 111, as local:qresource.cpp:QResourceRoot
namespace {
class QResourceRoot
{
public:
    enum Flags {
        // must match rcc.h
        Compressed = 0x01,
        Directory = 0x02,
        CompressedZstd = 0x04
    };

private:
    const uchar *tree, *names, *payloads;
    int version;
    inline int findOffset(int node) const { return node * (14 + (version >= 0x02 ? 8 : 0)); } //sizeof each tree element
    uint hash(int node) const;
    QString name(int node) const;
    bool nameMatches(int node, QStringView other) const;
    short flags(int node) const;
public:
    mutable QAtomicInt ref;

    inline QResourceRoot(): tree(nullptr), names(nullptr), payloads(nullptr), version(0) {}
    inline QResourceRoot(int version, const uchar *t, const uchar *n, const uchar *d) { setSource(version, t, n, d); }
    virtual ~QResourceRoot() = default;
    Q_DISABLE_COPY_MOVE(QResourceRoot)
    int findNode(const QString &path, const QLocale &locale) const;
    inline bool isContainer(int node) const { return flags(node) & Directory; }
    QResource::Compression compressionAlgo(int node)
    {
        uint compressionFlags = flags(node) & (Compressed | CompressedZstd);
        if (compressionFlags == Compressed)
            return QResource::ZlibCompression;
        if (compressionFlags == CompressedZstd)
            return QResource::ZstdCompression;
        return QResource::NoCompression;
    }
    const uchar *data(int node, qint64 *size) const;
    qint64 lastModified(int node) const;
    QStringList children(int node) const;
    virtual QStringView mappingRoot() const { return {}; }
    bool mappingRootSubdir(const QString &path, QString *match = nullptr) const;
    inline bool operator==(const QResourceRoot &other) const
    { return tree == other.tree && names == other.names && payloads == other.payloads && version == other.version; }
    inline bool operator!=(const QResourceRoot &other) const
    { return !operator==(other); }
    enum ResourceRootType { Resource_Builtin, Resource_File, Resource_Buffer };
    virtual ResourceRootType type() const { return Resource_Builtin; }

protected:
    inline void setSource(int v, const uchar *t, const uchar *n, const uchar *d) {
        tree = t;
        names = n;
        payloads = d;
        version = v;
    }
};
}  // namespace

//  from src/corelib/io/qresource.cpp, line 168, as local:qresource.cpp:cleanPath
namespace {
static QString cleanPath(const QString &_path)
{
    QString path = QDir::cleanPath(_path);
    // QDir::cleanPath does not remove two trailing slashes under _Windows_
    // due to support for UNC paths. Remove those manually.
    if (path.startsWith("//"_L1))
        path.remove(0, 1);
    return path;
}
}  // namespace

//  from src/corelib/io/qresource.cpp, line 285, as local:qresource.cpp:QResourcePrivate
class QResourcePrivate {
public:
    inline QResourcePrivate(QResource *_q, const QString &file, const QLocale &locale)
        : locale(locale), fileName(file), q_ptr(_q)
    {
        clear();
    }
    inline ~QResourcePrivate() { clear(); }

    void ensureInitialized() const;
    void ensureChildren() const;
    Q_DECL_PURE_FUNCTION qint64 uncompressedSize() const;
    qsizetype decompress(char *buffer, qsizetype bufferSize) const;

    bool load(const QString &file);
    void clear();

    static bool mayRemapData(const QResource &resource);

    QLocale locale;
    QString fileName, absoluteFilePath;
    QVarLengthArray<QResourceRoot *, 1> related;
    qint64 size;
    qint64 lastModified;
    const uchar *data;
    mutable QStringList children;
    quint8 compressionAlgo;
    bool container;
    /* 2 or 6 padding bytes */

    QResource *q_ptr;
    Q_DECLARE_PUBLIC(QResource)
};

//  from src/corelib/io/qresource.cpp, line 433, as local:qresource.cpp:QResourcePrivate::uncompressedSize
inline qint64 QResourcePrivate::uncompressedSize() const
{
    switch (compressionAlgo) {
    case QResource::NoCompression:
        return size;

    case QResource::ZlibCompression:
#ifndef QT_NO_COMPRESS
        if (size_t(size) >= sizeof(quint32))
            return qFromBigEndian<quint32>(data);
#else
        Q_ASSERT(!"QResource: Qt built without support for Zlib compression");
        Q_UNREACHABLE();
#endif
        break;

    case QResource::ZstdCompression: {
#if QT_CONFIG(zstd)
        size_t n = ZSTD_getFrameContentSize(data, size);
        return ZSTD_isError(n) ? -1 : qint64(n);
#else
        // This should not happen because we've refused to load such resource
        Q_ASSERT(!"QResource: Qt built without support for Zstd compression");
        Q_UNREACHABLE();
#endif
    }
    }
    return -1;
}

//  from src/corelib/io/qresource.cpp, line 463, as local:qresource.cpp:QResourcePrivate::decompress
inline qsizetype QResourcePrivate::decompress(char *buffer, qsizetype bufferSize) const
{
    Q_ASSERT(data);
#if defined(QT_NO_COMPRESS) && !QT_CONFIG(zstd)
    Q_UNUSED(buffer);
    Q_UNUSED(bufferSize);
#endif

    switch (compressionAlgo) {
    case QResource::NoCompression:
        Q_UNREACHABLE();
        break;

    case QResource::ZlibCompression: {
#ifndef QT_NO_COMPRESS
        uLong len = uLong(bufferSize);
        int res = ::uncompress(reinterpret_cast<Bytef *>(buffer), &len, data + sizeof(quint32),
                               uLong(size - sizeof(quint32)));
        if (res != Z_OK) {
            qWarning("QResource: error decompressing zlib content (%d)", res);
            return -1;
        }
        return len;
#else
        Q_UNREACHABLE();
#endif
    }

    case QResource::ZstdCompression: {
#if QT_CONFIG(zstd)
        size_t usize = ZSTD_decompress(buffer, bufferSize, data, size);
        if (ZSTD_isError(usize)) {
            qWarning("QResource: error decompressing zstd content: %s", ZSTD_getErrorName(usize));
            return -1;
        }
        return usize;
#else
        Q_UNREACHABLE();
#endif
    }
    }

    return -1;
}

//  from src/corelib/io/qresource.cpp, line 768, as local:qresource.cpp:QResourceRoot::hash
inline uint QResourceRoot::hash(int node) const
{
    if (!node) // root
        return 0;
    const int offset = findOffset(node);
    qint32 name_offset = qFromBigEndian<qint32>(tree + offset);
    name_offset += 2; // jump past name length
    return qFromBigEndian<quint32>(names + name_offset);
}

//  from src/corelib/io/qresource.cpp, line 777, as local:qresource.cpp:QResourceRoot::name
inline QString QResourceRoot::name(int node) const
{
    if (!node) // root
        return QString();
    const int offset = findOffset(node);

    QString ret;
    qint32 name_offset = qFromBigEndian<qint32>(tree + offset);
    quint16 name_length = qFromBigEndian<qint16>(names + name_offset);
    name_offset += 2;
    name_offset += 4; // jump past hash

    ret.resize(name_length);
    QChar *strData = ret.data();
    qFromBigEndian<char16_t>(names + name_offset, name_length, strData);
    return ret;
}

//  from src/corelib/io/qresource.cpp, line 795, as local:qresource.cpp:QResourceRoot::nameMatches
inline bool QResourceRoot::nameMatches(int node, QStringView other) const
{
    if (!node) // root
        return other.isEmpty();
    const int offset = findOffset(node);

    qint32 name_offset = qFromBigEndian<qint32>(tree + offset);
    qsizetype name_length = qFromBigEndian<qint16>(names + name_offset);
    name_offset += 2;
    name_offset += 4; //jump past hash

    if (other.size() != name_length)
        return false;
    const QChar *strData = reinterpret_cast<const QChar *>(names + name_offset);
    for (qsizetype ch = 0; ch < name_length; ++ch) {
        if (other.at(ch) != qFromBigEndian<char16_t>(strData + ch))
            return false;
    }
    return true;
}

//  from src/corelib/io/qresource.cpp, line 816, as local:qresource.cpp:QResourceRoot::findNode
inline int QResourceRoot::findNode(const QString &_path, const QLocale &locale) const
{
    QStringView path = _path;
    {
        const QStringView root = mappingRoot();
        if (!root.isEmpty()) {
            if (root == path) {
                path = u"/"_sv;
            } else {
                const bool rootEndsWithSlash = root.endsWith(u'/');
                const qsizetype prefixLength = root.size() + !rootEndsWithSlash;
                if (path.size() >= prefixLength && path.startsWith(root)
                    && (rootEndsWithSlash || path.at(root.size()) == u'/')) {
                    path = path.sliced(prefixLength - 1);
                }
                if (path.isEmpty())
                    path = u"/"_sv;
            }
        }
    }
#ifdef DEBUG_RESOURCE_MATCH
    qDebug() << "!!!!" << "START" << path << locale.territory() << locale.language();
#endif

    if (path == "/"_L1)
        return 0;

    // the root node is always first
    qint32 child_count = qFromBigEndian<qint32>(tree + 6);
    qint32 child       = qFromBigEndian<qint32>(tree + 10);

    // now iterate up the tree
    int node = -1;

    QStringSplitter splitter(path);
    while (child_count && splitter.hasNext()) {
        QStringView segment = splitter.next();

#ifdef DEBUG_RESOURCE_MATCH
        qDebug() << "  CHILDREN" << segment;
        for (int j = 0; j < child_count; ++j) {
            qDebug() << "   " << child + j << " :: " << name(child + j);
        }
#endif
        const uint h = qt_hash(segment);

        // do the binary search for the hash
        int l = 0, r = child_count - 1;
        int sub_node = (l + r + 1) / 2;
        while (r != l) {
            const uint sub_node_hash = hash(child + sub_node);
            if (h == sub_node_hash)
                break;
            else if (h < sub_node_hash)
                r = sub_node - 1;
            else
                l = sub_node;
            sub_node = (l + r + 1) / 2;
        }
        sub_node += child;

        // now do the "harder" compares
        bool found = false;
        if (hash(sub_node) == h) {
            while (sub_node > child && hash(sub_node - 1) == h) // backup for collisions
                --sub_node;
            for (; sub_node < child + child_count && hash(sub_node) == h;
                 ++sub_node) { // here we go...
                if (nameMatches(sub_node, segment)) {
                    found = true;
                    int offset = findOffset(sub_node);
#ifdef DEBUG_RESOURCE_MATCH
                    qDebug() << "  TRY" << sub_node << name(sub_node) << offset;
#endif
                    offset += 4; // jump past name

                    const qint16 flags = qFromBigEndian<qint16>(tree + offset);
                    offset += 2;

                    if (!splitter.hasNext()) {
                        if (!(flags & Directory)) {
                            const qint16 territory = qFromBigEndian<qint16>(tree + offset);
                            offset += 2;

                            const qint16 language = qFromBigEndian<qint16>(tree + offset);
                            offset += 2;
#ifdef DEBUG_RESOURCE_MATCH
                            qDebug() << "    " << "LOCALE" << country << language;
#endif
                            if (territory == locale.territory() && language == locale.language()) {
#ifdef DEBUG_RESOURCE_MATCH
                                qDebug() << "!!!!" << "FINISHED" << __LINE__ << sub_node;
#endif
                                return sub_node;
                            } else if ((territory == QLocale::AnyTerritory
                                        && language == locale.language())
                                       || (territory == QLocale::AnyTerritory
                                           && language == QLocale::C
                                           && node == -1)) {
                                node = sub_node;
                            }
                            continue;
                        } else {
#ifdef DEBUG_RESOURCE_MATCH
                            qDebug() << "!!!!" << "FINISHED" << __LINE__ << sub_node;
#endif

                            return sub_node;
                        }
                    }

                    if (!(flags & Directory))
                        return -1;

                    child_count = qFromBigEndian<qint32>(tree + offset);
                    offset += 4;
                    child = qFromBigEndian<qint32>(tree + offset);
                    break;
                }
            }
        }
        if (!found)
            break;
    }
#ifdef DEBUG_RESOURCE_MATCH
    qDebug() << "!!!!" << "FINISHED" << __LINE__ << node;
#endif
    return node;
}

//  from src/corelib/io/qresource.cpp, line 945, as local:qresource.cpp:QResourceRoot::flags
inline short QResourceRoot::flags(int node) const
{
    if (node == -1)
        return 0;
    const int offset = findOffset(node) + 4; // jump past name
    return qFromBigEndian<qint16>(tree + offset);
}

//  from src/corelib/io/qresource.cpp, line 952, as local:qresource.cpp:QResourceRoot::data
inline const uchar *QResourceRoot::data(int node, qint64 *size) const
{
    if (node == -1) {
        *size = 0;
        return nullptr;
    }
    int offset = findOffset(node) + 4; // jump past name

    const qint16 flags = qFromBigEndian<qint16>(tree + offset);
    offset += 2;

    offset += 4; // jump past locale

    if (!(flags & Directory)) {
        const qint32 data_offset = qFromBigEndian<qint32>(tree + offset);
        const quint32 data_length = qFromBigEndian<quint32>(payloads + data_offset);
        const uchar *ret = payloads + data_offset + 4;
        *size = data_length;
        return ret;
    }
    *size = 0;
    return nullptr;
}

//  from src/corelib/io/qresource.cpp, line 976, as local:qresource.cpp:QResourceRoot::lastModified
inline qint64 QResourceRoot::lastModified(int node) const
{
    if (node == -1 || version < 0x02)
        return 0;

    const int offset = findOffset(node) + 14;

    return qFromBigEndian<qint64>(tree + offset);
}

//  from src/corelib/io/qresource.cpp, line 986, as local:qresource.cpp:QResourceRoot::children
inline QStringList QResourceRoot::children(int node) const
{
    if (node == -1)
        return QStringList();
    int offset = findOffset(node) + 4; // jump past name

    const qint16 flags = qFromBigEndian<qint16>(tree + offset);
    offset += 2;

    QStringList ret;
    if (flags & Directory) {
        const qint32 child_count = qFromBigEndian<qint32>(tree + offset);
        offset += 4;
        const qint32 child_off = qFromBigEndian<qint32>(tree + offset);
        ret.reserve(child_count);
        for (int i = child_off; i < child_off + child_count; ++i)
            ret << name(i);
    }
    return ret;
}

//  from src/corelib/io/qresource.cpp, line 1081, as local:qresource.cpp:QDynamicBufferResourceRoot
namespace {
class QDynamicBufferResourceRoot : public QResourceRoot
{
    QString root;
    const uchar *buffer;

public:
    inline QDynamicBufferResourceRoot(const QString &_root) : root(_root), buffer(nullptr) { }
    inline ~QDynamicBufferResourceRoot() { }
    inline const uchar *mappingBuffer() const { return buffer; }
    QStringView mappingRoot() const override { return root; }
    ResourceRootType type() const override { return Resource_Buffer; }

    // size == -1 means "unknown"
    bool registerSelf(const uchar *b, qsizetype size, const QString &source = {})
    {
        // 5 int "pointers"
        if (size >= 0 && size < 20)
            return false;

        // setup the data now
        int offset = 0;

        // magic number
        if (b[offset + 0] != 'q' || b[offset + 1] != 'r' || b[offset + 2] != 'e'
            || b[offset + 3] != 's') {
            return false;
        }
        offset += 4;

        const int version = qFromBigEndian<qint32>(b + offset);
        offset += 4;

        const int tree_offset = qFromBigEndian<qint32>(b + offset);
        offset += 4;

        const int data_offset = qFromBigEndian<qint32>(b + offset);
        offset += 4;

        const int name_offset = qFromBigEndian<qint32>(b + offset);
        offset += 4;

        quint32 file_flags = 0;
        if (version >= 3) {
            file_flags = qFromBigEndian<qint32>(b + offset);
            offset += 4;
        }

        // Some sanity checking for sizes. This is _not_ a security measure.
        if (size >= 0 && (tree_offset >= size || data_offset >= size || name_offset >= size))
            return false;

        // And some sanity checking for features
        quint32 acceptableFlags = 0;
#ifndef QT_NO_COMPRESS
        acceptableFlags |= Compressed;
#endif
        if (QT_CONFIG(zstd))
            acceptableFlags |= CompressedZstd;
        if (const quint32 unsupportedFlags = file_flags & ~acceptableFlags) {
            const QString id = source.isEmpty() ? QString::asprintf("<buffer at %p>", b) : source;
            qWarning("QResource: %s uses unsupported compression flags 0x%x (supported: 0x%x)",
                     qUtf8Printable(id), unsupportedFlags, acceptableFlags);
            return false;
        }

        if (version >= 0x01 && version <= 0x03) {
            buffer = b;
            setSource(version, b + tree_offset, b + name_offset, b + data_offset);
            return true;
        }
        return false;
    }
};
}  // namespace

//  from src/corelib/io/qresource.cpp, line 1414, as local:qresource.cpp:QResourceFileEnginePrivate
#if !defined(QT_BOOTSTRAPPED)
class QResourceFileEnginePrivate : public QAbstractFileEnginePrivate
{
protected:
    Q_DECLARE_PUBLIC(QResourceFileEngine)
private:
    uchar *map(qint64 offset, qint64 size, QFile::MemoryMapFlags flags);
    bool unmap(uchar *ptr);
    void uncompress() const;
    void mapUncompressed();
    bool mapUncompressed_sys();
    void unmapUncompressed_sys();
    qint64 offset = 0;
    QResource resource;
    mutable QByteArray uncompressed;
    bool mustUnmap = false;

    // minimum size for which we'll try to re-open ourselves in mapUncompressed()
    static constexpr qsizetype RemapCompressedThreshold = 16384;
protected:
    QResourceFileEnginePrivate(QAbstractFileEngine *q) :
        QAbstractFileEnginePrivate(q) {}

    ~QResourceFileEnginePrivate()
    {
        if (mustUnmap)
            unmapUncompressed_sys();
    }
};
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1649, as local:qresource.cpp:QResourceFileEnginePrivate::map
#if !defined(QT_BOOTSTRAPPED)
inline uchar *QResourceFileEnginePrivate::map(qint64 offset, qint64 size, QFile::MemoryMapFlags flags)
{
    Q_Q(QResourceFileEngine);
    Q_ASSERT_X(resource.compressionAlgorithm() == QResource::NoCompression
               || !uncompressed.isNull(), "QFile::map()",
               "open() should have uncompressed compressed resources");

    qint64 max = resource.uncompressedSize();
    qint64 end;
    if (offset < 0 || size <= 0 || !resource.isValid() ||
            qAddOverflow(offset, size, &end) || end > max) {
        q->setError(QFile::UnspecifiedError, QString());
        return nullptr;
    }

    const uchar *address = reinterpret_cast<const uchar *>(uncompressed.constBegin());
    if (!uncompressed.isNull())
        return const_cast<uchar *>(address) + offset;

    // resource was not compressed
    address = resource.data();
    if (flags & QFile::MapPrivateOption) {
        // We need to provide read-write memory
        mapUncompressed();
        address = reinterpret_cast<const uchar *>(uncompressed.constData());
    }

    return const_cast<uchar *>(address) + offset;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1679, as local:qresource.cpp:QResourceFileEnginePrivate::unmap
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEnginePrivate::unmap(uchar *ptr)
{
    Q_UNUSED(ptr);
    return true;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1685, as local:qresource.cpp:QResourceFileEnginePrivate::uncompress
#if !defined(QT_BOOTSTRAPPED)
inline void QResourceFileEnginePrivate::uncompress() const
{
    if (resource.compressionAlgorithm() == QResource::NoCompression
            || !uncompressed.isEmpty() || resource.size() == 0)
        return;     // nothing to do
    uncompressed = resource.uncompressedData();
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1693, as local:qresource.cpp:QResourceFileEnginePrivate::mapUncompressed
#if !defined(QT_BOOTSTRAPPED)
inline void QResourceFileEnginePrivate::mapUncompressed()
{
    Q_ASSERT(resource.compressionAlgorithm() == QResource::NoCompression);
    if (!uncompressed.isNull())
        return;     // nothing to do

    if (resource.uncompressedSize() >= RemapCompressedThreshold) {
        if (mapUncompressed_sys())
            return;
    }

    uncompressed = resource.uncompressedData();
    uncompressed.detach();
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1734, as local:qresource.cpp:mappingBoundaries
#if !defined(QT_BOOTSTRAPPED)
#if defined(Q_OS_LINUX)
static auto mappingBoundaries(const void *location, qsizetype size)
{
#ifdef Q_OS_WIN
    auto getpagesize = [] {
        SYSTEM_INFO sysinfo;
        ::GetSystemInfo(&sysinfo);
        return sysinfo.dwAllocationGranularity;
    };
#endif
    struct R {
        void *begin;
        qsizetype size;
        qptrdiff offset;
    } r;

    const quintptr pageMask = getpagesize() - 1;
    quintptr data = quintptr(location);
    quintptr begin = data & ~pageMask;
    quintptr end = (data + size + pageMask) & ~pageMask;
    r.begin = reinterpret_cast<void *>(begin);
    r.size = end - begin;
    r.offset = data & pageMask;
    return r;
}
#endif  // defined(Q_OS_LINUX)
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1759, as local:qresource.cpp:QResourceFileEnginePrivate::mapUncompressed_sys
#if !defined(QT_BOOTSTRAPPED)
#if defined(Q_OS_LINUX)
inline bool QResourceFileEnginePrivate::mapUncompressed_sys()
{
    auto r = mappingBoundaries(resource.data(), resource.uncompressedSize());
    void *ptr = nullptr;

#if defined(MREMAP_MAYMOVE) && defined(MREMAP_DONTUNMAP)
    // Use MREMAP_MAYMOVE to tell the kernel to give us a new address and use
    // MREMAP_DONTUNMAP (supported since kernel 5.7) to request that it create
    // a new mapping of the same pages, instead of moving. We can only do that
    // for pages that are read-only, otherwise the kernel replaces the source
    // with pages full of nulls.
    if (!QResourcePrivate::mayRemapData(resource))
        return false;

    ptr = mremap(r.begin, r.size, r.size, MREMAP_MAYMOVE | MREMAP_DONTUNMAP);
    if (ptr == MAP_FAILED)
        return false;

    // Allow writing, which the documentation says we allow. This is safe
    // because MREMAP_DONTUNMAP only works for private mappings.
    if (mprotect(ptr, r.size, PROT_READ | PROT_WRITE) != 0) {
        munmap(ptr, r.size);
        return false;
    }
#elif defined(Q_OS_DARWIN)
    mach_port_t self = mach_task_self();
    vm_address_t addr = 0;
    vm_address_t mask = 0;
    bool anywhere = true;
    bool copy = true;
    vm_prot_t cur_prot = VM_PROT_READ | VM_PROT_WRITE;
    vm_prot_t max_prot = VM_PROT_ALL;
    kern_return_t res = vm_remap(self, &addr, r.size, mask, anywhere,
                                 self, vm_address_t(r.begin), copy, &cur_prot,
                                 &max_prot, VM_INHERIT_DEFAULT);
    if (res != KERN_SUCCESS)
        return false;

    ptr = reinterpret_cast<void *>(addr);
    if ((max_prot & VM_PROT_WRITE) == 0 || mprotect(ptr, r.size, PROT_READ | PROT_WRITE) != 0) {
        munmap(ptr, r.size);
        return false;
    }
#endif

    if (!ptr)
        return false;
    const char *newdata = static_cast<char *>(ptr) + r.offset;
    uncompressed = QByteArray::fromRawData(newdata, resource.uncompressedSize());
    mustUnmap = true;
    return true;
}
#endif  // defined(Q_OS_LINUX)
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1459, as _ZN19QResourceFileEngine11setFileNameERK7QString
#if !defined(QT_BOOTSTRAPPED)
inline void QResourceFileEngine::setFileName(const QString &file)
{
    Q_D(QResourceFileEngine);
    d->resource.setFileName(file);
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1491, as _ZN19QResourceFileEngine5closeEv
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::close()
{
    Q_D(QResourceFileEngine);
    d->offset = 0;
    return true;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1498, as _ZN19QResourceFileEngine5flushEv
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::flush()
{
    return true;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1518, as _ZNK19QResourceFileEngine4sizeEv
#if !defined(QT_BOOTSTRAPPED)
inline qint64 QResourceFileEngine::size() const
{
    Q_D(const QResourceFileEngine);
    return d->resource.isValid() ? d->resource.uncompressedSize() : 0;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1524, as _ZNK19QResourceFileEngine3posEv
#if !defined(QT_BOOTSTRAPPED)
inline qint64 QResourceFileEngine::pos() const
{
    Q_D(const QResourceFileEngine);
    return d->offset;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1530, as _ZNK19QResourceFileEngine5atEndEv
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::atEnd() const
{
    Q_D(const QResourceFileEngine);
    if (!d->resource.isValid())
        return true;
    return d->offset == size();
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1538, as _ZN19QResourceFileEngine4seekEx
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::seek(qint64 pos)
{
    Q_D(QResourceFileEngine);
    if (!d->resource.isValid())
        return false;

    if (d->offset > size())
        return false;
    d->offset = pos;
    return true;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1503, as _ZN19QResourceFileEngine4readEPcx
#if !defined(QT_BOOTSTRAPPED)
inline qint64 QResourceFileEngine::read(char *data, qint64 len)
{
    Q_D(QResourceFileEngine);
    if (len > size() - d->offset)
        len = size() - d->offset;
    if (len <= 0)
        return 0;
    if (!d->uncompressed.isNull())
        memcpy(data, d->uncompressed.constData() + d->offset, len);
    else
        memcpy(data, d->resource.data() + d->offset, len);
    d->offset += len;
    return len;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1443, as _ZNK19QResourceFileEngine13caseSensitiveEv
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::caseSensitive() const
{
    return true;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1550, as _ZNK19QResourceFileEngine9fileFlagsE6QFlagsIN19QAbstractFileEngine8FileFlagEE
#if !defined(QT_BOOTSTRAPPED)
inline QAbstractFileEngine::FileFlags QResourceFileEngine::fileFlags(QAbstractFileEngine::FileFlags type) const
{
    Q_D(const QResourceFileEngine);
    QAbstractFileEngine::FileFlags ret;
    if (!d->resource.isValid())
        return ret;

    if (type & PermsMask)
        ret |= QAbstractFileEngine::FileFlags(ReadOwnerPerm | ReadUserPerm | ReadGroupPerm
                                              | ReadOtherPerm);
    if (type & TypesMask) {
        if (d->resource.isDir())
            ret |= DirectoryType;
        else
            ret |= FileType;
    }
    if (type & FlagsMask) {
        ret |= ExistsFlag;
        if (d->resource.absoluteFilePath() == ":/"_L1)
            ret |= RootFlag;
    }
    return ret;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1574, as _ZNK19QResourceFileEngine8fileNameEN19QAbstractFileEngine8FileNameE
#if !defined(QT_BOOTSTRAPPED)
inline QString QResourceFileEngine::fileName(FileName file) const
{
    Q_D(const QResourceFileEngine);
    if (file == BaseName) {
        const qsizetype slash = d->resource.fileName().lastIndexOf(u'/');
        if (slash == -1)
            return d->resource.fileName();
        return d->resource.fileName().mid(slash + 1);
    } else if (file == PathName || file == AbsolutePathName) {
        const QString path = (file == AbsolutePathName) ? d->resource.absoluteFilePath()
                                                        : d->resource.fileName();
        const qsizetype slash = path.lastIndexOf(u'/');
        if (slash == -1)
            return ":"_L1;
        else if (slash <= 1)
            return ":/"_L1;
        return path.left(slash);

    } else if (file == CanonicalName || file == CanonicalPathName) {
        const QString absoluteFilePath = d->resource.absoluteFilePath();
        if (file == CanonicalPathName) {
            const qsizetype slash = absoluteFilePath.lastIndexOf(u'/');
            if (slash != -1)
                return absoluteFilePath.left(slash);
        }
        return absoluteFilePath;
    }
    return d->resource.fileName();
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1604, as _ZNK19QResourceFileEngine7ownerIdEN19QAbstractFileEngine9FileOwnerE
#if !defined(QT_BOOTSTRAPPED)
inline uint QResourceFileEngine::ownerId(FileOwner) const
{
    static const uint nobodyID = static_cast<uint>(-2);
    return nobodyID;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1628, as _ZN19QResourceFileEngine9extensionEN19QAbstractFileEngine9ExtensionEPKNS0_15ExtensionOptionEPNS0_15ExtensionReturnE
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::extension(Extension extension, const ExtensionOption *option, ExtensionReturn *output)
{
    Q_D(QResourceFileEngine);
    if (extension == MapExtension) {
        const auto *options = static_cast<const MapExtensionOption *>(option);
        auto *returnValue = static_cast<MapExtensionReturn *>(output);
        returnValue->address = d->map(options->offset, options->size, options->flags);
        return (returnValue->address != nullptr);
    }
    if (extension == UnMapExtension) {
        const auto *options = static_cast<const UnMapExtensionOption *>(option);
        return d->unmap(options->address);
    }
    return false;
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1644, as _ZNK19QResourceFileEngine17supportsExtensionEN19QAbstractFileEngine9ExtensionE
#if !defined(QT_BOOTSTRAPPED)
inline bool QResourceFileEngine::supportsExtension(Extension extension) const
{
    return (extension == UnMapExtension || extension == MapExtension);
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  from src/corelib/io/qresource.cpp, line 1455, as _ZN19QResourceFileEngineD1Ev
#if !defined(QT_BOOTSTRAPPED)
inline QResourceFileEngine::~QResourceFileEngine()
{
}
#endif  // !defined(QT_BOOTSTRAPPED)
//  -----------------------------------------------------------------------

//  A QResourceFileEngine that Python can take functions over in. Every QResourceFileEngine
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQResourceFileEngineCall0)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall1)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall2)(const void *, int *);
typedef qint64 (*CuteQResourceFileEngineCall3)(const void *, int *);
typedef qint64 (*CuteQResourceFileEngineCall4)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall5)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall6)(const void *, qint64, int *);
typedef qint64 (*CuteQResourceFileEngineCall7)(const void *, char *, qint64, int *);
typedef bool (*CuteQResourceFileEngineCall8)(const void *, int *);
typedef int (*CuteQResourceFileEngineCall9)(const void *, int, int *);
typedef QString * (*CuteQResourceFileEngineCall10)(const void *, int, int *);
typedef uint (*CuteQResourceFileEngineCall11)(const void *, int, int *);
typedef bool (*CuteQResourceFileEngineCall12)(const void *, int, const QAbstractFileEngine::ExtensionOption *, QAbstractFileEngine::ExtensionReturn *, int *);
typedef bool (*CuteQResourceFileEngineCall13)(const void *, int, int *);
typedef bool (*CuteQResourceFileEngineCall14)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall15)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall16)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall17)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall18)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall19)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall20)(const void *, const QString *, int *);
typedef bool (*CuteQResourceFileEngineCall21)(const void *, const QString *, bool, int *);
typedef bool (*CuteQResourceFileEngineCall22)(const void *, qint64, int *);
typedef bool (*CuteQResourceFileEngineCall23)(const void *, int *);
typedef bool (*CuteQResourceFileEngineCall24)(const void *, uint, int *);
typedef const QByteArray * (*CuteQResourceFileEngineCall25)(const void *, int *);
typedef QString * (*CuteQResourceFileEngineCall26)(const void *, int, int *);
typedef int (*CuteQResourceFileEngineCall27)(const void *, int *);
typedef int (*CuteQResourceFileEngineCall28)(const void *, QAbstractFileEngine *, int *);
typedef qint64 (*CuteQResourceFileEngineCall29)(const void *, char *, qint64, int *);
class CuteQResourceFileEngine : public QResourceFileEngine {
public:
  using QResourceFileEngine::QResourceFileEngine;
  void *taken[30] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine11setFileNameERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5closeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine5flushEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine4sizeEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine3posEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5atEndEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4seekEx")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4readEPcx")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine13caseSensitiveEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine9fileFlagsE6QFlagsINS_8FileFlagEE")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine8fileNameENS_8FileNameE")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine7ownerIdENS_9FileOwnerE")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine9extensionENS_9ExtensionEPKNS_15ExtensionOptionEPNS_15ExtensionReturnE")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine17supportsExtensionENS_9ExtensionE")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine10syncToDiskEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine12isSequentialEv")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6removeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4copyERK7QString")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine6renameERK7QString")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine15renameOverwriteERK7QString")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine4linkERK7QString")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5rmdirERK7QStringb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7setSizeEx")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine14isRelativePathEv")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine14setPermissionsEj")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine2idEv")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine5ownerENS_9FileOwnerE")) {
      taken[26] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK19QAbstractFileEngine6handleEv")) {
      taken[27] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine7cloneToEPS_")) {
      taken[28] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN19QAbstractFileEngine8readLineEPcx")) {
      taken[29] = call;
      return true;
    }
    return false;
  }

  //  void QResourceFileEngine::setFileName(const QString &file)
  void setFileName(const QString &file) override {
    if (taken[0]) {
      int handled = 0;
      CuteQResourceFileEngineCall0 call = reinterpret_cast<CuteQResourceFileEngineCall0>(taken[0]);
      call(this, &file, &handled);
      if (handled) return;
    }
    QResourceFileEngine::setFileName(file);
  }

  //  bool QResourceFileEngine::close()
  bool close() override {
    if (taken[1]) {
      int handled = 0;
      CuteQResourceFileEngineCall1 call = reinterpret_cast<CuteQResourceFileEngineCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::close();
  }

  //  bool QResourceFileEngine::flush()
  bool flush() override {
    if (taken[2]) {
      int handled = 0;
      CuteQResourceFileEngineCall2 call = reinterpret_cast<CuteQResourceFileEngineCall2>(taken[2]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::flush();
  }

  //  qint64 QResourceFileEngine::size() const
  qint64 size() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQResourceFileEngineCall3 call = reinterpret_cast<CuteQResourceFileEngineCall3>(taken[3]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::size();
  }

  //  qint64 QResourceFileEngine::pos() const
  qint64 pos() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQResourceFileEngineCall4 call = reinterpret_cast<CuteQResourceFileEngineCall4>(taken[4]);
      qint64 given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::pos();
  }

  //  bool QResourceFileEngine::atEnd() const
  bool atEnd() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQResourceFileEngineCall5 call = reinterpret_cast<CuteQResourceFileEngineCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::atEnd();
  }

  //  bool QResourceFileEngine::seek(qint64 a0)
  bool seek(qint64 a0) override {
    if (taken[6]) {
      int handled = 0;
      CuteQResourceFileEngineCall6 call = reinterpret_cast<CuteQResourceFileEngineCall6>(taken[6]);
      bool given = call(this, a0, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::seek(a0);
  }

  //  qint64 QResourceFileEngine::read(char *data, qint64 maxlen)
  qint64 read(char *data, qint64 maxlen) override {
    if (taken[7]) {
      int handled = 0;
      CuteQResourceFileEngineCall7 call = reinterpret_cast<CuteQResourceFileEngineCall7>(taken[7]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::read(data, maxlen);
  }

  //  bool QResourceFileEngine::caseSensitive() const
  bool caseSensitive() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQResourceFileEngineCall8 call = reinterpret_cast<CuteQResourceFileEngineCall8>(taken[8]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::caseSensitive();
  }

  //  FileFlags QResourceFileEngine::fileFlags(FileFlags type) const
  QAbstractFileEngine::FileFlags fileFlags(
      QAbstractFileEngine::FileFlags type) const override {
    if (taken[9]) {
      int handled = 0;
      CuteQResourceFileEngineCall9 call = reinterpret_cast<CuteQResourceFileEngineCall9>(taken[9]);
      int given = call(this, static_cast<int>(type.toInt()), &handled);
      if (handled) return QFlags<QAbstractFileEngine::FileFlag>::fromInt(given);
    }
    return QResourceFileEngine::fileFlags(type);
  }

  //  QString QResourceFileEngine::fileName(QAbstractFileEngine::FileName
  //      file) const
  QString fileName(QAbstractFileEngine::FileName file) const override {
    if (taken[10]) {
      int handled = 0;
      CuteQResourceFileEngineCall10 call = reinterpret_cast<CuteQResourceFileEngineCall10>(taken[10]);
      QString * given = call(this, static_cast<int>(file), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QResourceFileEngine::fileName(file);
  }

  //  uint QResourceFileEngine::ownerId(FileOwner a0) const
  uint ownerId(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[11]) {
      int handled = 0;
      CuteQResourceFileEngineCall11 call = reinterpret_cast<CuteQResourceFileEngineCall11>(taken[11]);
      uint given = call(this, static_cast<int>(a0), &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::ownerId(a0);
  }

  //  bool QResourceFileEngine::extension(Extension extension, const
  //      ExtensionOption *option, ExtensionReturn *output)
  bool extension(
      QAbstractFileEngine::Extension extension,
      const QAbstractFileEngine::ExtensionOption *option,
      QAbstractFileEngine::ExtensionReturn *output) override {
    if (taken[12]) {
      int handled = 0;
      CuteQResourceFileEngineCall12 call = reinterpret_cast<CuteQResourceFileEngineCall12>(taken[12]);
      bool given = call(this, static_cast<int>(extension), option, output, &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::extension(extension, option, output);
  }

  //  bool QResourceFileEngine::supportsExtension(Extension extension)
  //      const
  bool supportsExtension(
      QAbstractFileEngine::Extension extension) const override {
    if (taken[13]) {
      int handled = 0;
      CuteQResourceFileEngineCall13 call = reinterpret_cast<CuteQResourceFileEngineCall13>(taken[13]);
      bool given = call(this, static_cast<int>(extension), &handled);
      if (handled) return given;
    }
    return QResourceFileEngine::supportsExtension(extension);
  }

  //  bool QAbstractFileEngine::syncToDisk()
  bool syncToDisk() override {
    if (taken[14]) {
      int handled = 0;
      CuteQResourceFileEngineCall14 call = reinterpret_cast<CuteQResourceFileEngineCall14>(taken[14]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::syncToDisk();
  }

  //  bool QAbstractFileEngine::isSequential() const
  bool isSequential() const override {
    if (taken[15]) {
      int handled = 0;
      CuteQResourceFileEngineCall15 call = reinterpret_cast<CuteQResourceFileEngineCall15>(taken[15]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::isSequential();
  }

  //  bool QAbstractFileEngine::remove()
  bool remove() override {
    if (taken[16]) {
      int handled = 0;
      CuteQResourceFileEngineCall16 call = reinterpret_cast<CuteQResourceFileEngineCall16>(taken[16]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::remove();
  }

  //  bool QAbstractFileEngine::copy(const QString &newName)
  bool copy(const QString &newName) override {
    if (taken[17]) {
      int handled = 0;
      CuteQResourceFileEngineCall17 call = reinterpret_cast<CuteQResourceFileEngineCall17>(taken[17]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::copy(newName);
  }

  //  bool QAbstractFileEngine::rename(const QString &newName)
  bool rename(const QString &newName) override {
    if (taken[18]) {
      int handled = 0;
      CuteQResourceFileEngineCall18 call = reinterpret_cast<CuteQResourceFileEngineCall18>(taken[18]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::rename(newName);
  }

  //  bool QAbstractFileEngine::renameOverwrite(const QString &newName)
  bool renameOverwrite(const QString &newName) override {
    if (taken[19]) {
      int handled = 0;
      CuteQResourceFileEngineCall19 call = reinterpret_cast<CuteQResourceFileEngineCall19>(taken[19]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::renameOverwrite(newName);
  }

  //  bool QAbstractFileEngine::link(const QString &newName)
  bool link(const QString &newName) override {
    if (taken[20]) {
      int handled = 0;
      CuteQResourceFileEngineCall20 call = reinterpret_cast<CuteQResourceFileEngineCall20>(taken[20]);
      bool given = call(this, &newName, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::link(newName);
  }

  //  bool QAbstractFileEngine::rmdir(const QString &dirName, bool
  //      recurseParentDirectories) const
  bool rmdir(
      const QString &dirName,
      bool recurseParentDirectories) const override {
    if (taken[21]) {
      int handled = 0;
      CuteQResourceFileEngineCall21 call = reinterpret_cast<CuteQResourceFileEngineCall21>(taken[21]);
      bool given = call(this, &dirName, recurseParentDirectories, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::rmdir(dirName, recurseParentDirectories);
  }

  //  bool QAbstractFileEngine::setSize(qint64 size)
  bool setSize(qint64 size) override {
    if (taken[22]) {
      int handled = 0;
      CuteQResourceFileEngineCall22 call = reinterpret_cast<CuteQResourceFileEngineCall22>(taken[22]);
      bool given = call(this, size, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::setSize(size);
  }

  //  bool QAbstractFileEngine::isRelativePath() const
  bool isRelativePath() const override {
    if (taken[23]) {
      int handled = 0;
      CuteQResourceFileEngineCall23 call = reinterpret_cast<CuteQResourceFileEngineCall23>(taken[23]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::isRelativePath();
  }

  //  bool QAbstractFileEngine::setPermissions(uint perms)
  bool setPermissions(uint perms) override {
    if (taken[24]) {
      int handled = 0;
      CuteQResourceFileEngineCall24 call = reinterpret_cast<CuteQResourceFileEngineCall24>(taken[24]);
      bool given = call(this, perms, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::setPermissions(perms);
  }

  //  QByteArray QAbstractFileEngine::id() const
  QByteArray id() const override {
    if (taken[25]) {
      int handled = 0;
      CuteQResourceFileEngineCall25 call = reinterpret_cast<CuteQResourceFileEngineCall25>(taken[25]);
      const QByteArray * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QAbstractFileEngine::id();
  }

  //  QString QAbstractFileEngine::owner(FileOwner a0) const
  QString owner(QAbstractFileEngine::FileOwner a0) const override {
    if (taken[26]) {
      int handled = 0;
      CuteQResourceFileEngineCall26 call = reinterpret_cast<CuteQResourceFileEngineCall26>(taken[26]);
      QString * given = call(this, static_cast<int>(a0), &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QAbstractFileEngine::owner(a0);
  }

  //  int QAbstractFileEngine::handle() const
  int handle() const override {
    if (taken[27]) {
      int handled = 0;
      CuteQResourceFileEngineCall27 call = reinterpret_cast<CuteQResourceFileEngineCall27>(taken[27]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::handle();
  }

  //  TriStateResult QAbstractFileEngine::cloneTo(QAbstractFileEngine
  //      *target)
  QAbstractFileEngine::TriStateResult cloneTo(
      QAbstractFileEngine *target) override {
    if (taken[28]) {
      int handled = 0;
      CuteQResourceFileEngineCall28 call = reinterpret_cast<CuteQResourceFileEngineCall28>(taken[28]);
      int given = call(this, target, &handled);
      if (handled) return static_cast<QAbstractFileEngine::TriStateResult>(given);
    }
    return QAbstractFileEngine::cloneTo(target);
  }

  //  qint64 QAbstractFileEngine::readLine(char *data, qint64 maxlen)
  qint64 readLine(char *data, qint64 maxlen) override {
    if (taken[29]) {
      int handled = 0;
      CuteQResourceFileEngineCall29 call = reinterpret_cast<CuteQResourceFileEngineCall29>(taken[29]);
      qint64 given = call(this, data, maxlen, &handled);
      if (handled) return given;
    }
    return QAbstractFileEngine::readLine(data, maxlen);
  }
};

//  QResourceFileEnginePrivate *QResourceFileEngine::d_func()
extern "C" Q_DECL_EXPORT
QResourceFileEnginePrivate *ritual_ZN19QResourceFileEngine6d_funcEv(
    QResourceFileEngine *self) {
  return self->d_func();
}

//  const QResourceFileEnginePrivate *QResourceFileEngine::d_func() const
extern "C" Q_DECL_EXPORT
const QResourceFileEnginePrivate *ritual_ZNK19QResourceFileEngine6d_funcEv(
    const QResourceFileEngine *self) {
  return self->d_func();
}

//  QResourceFileEngine::~QResourceFileEngine()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QResourceFileEngineD1Ev(QResourceFileEngine *self) {
  delete self;
}

//  void QResourceFileEngine::setFileName(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QResourceFileEngine11setFileNameERK7QString(
    QResourceFileEngine *self,
    const QString *file) {
  self->setFileName(*file);
}

//  bool QResourceFileEngine::open(QIODevice::OpenMode flags,
//      std::optional<QFile::Permissions> permissions)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QResourceFileEngine4openE6QFlagsIN13QIODeviceBase12OpenModeFlagEESt8optionalIS0_IN11QFileDevice10PermissionEEE(
    QResourceFileEngine *self,
    int flags,
    const std::optional<QFile::Permissions> *permissions) {
  return self->open(
      QFlags<QIODeviceBase::OpenModeFlag>::fromInt(flags),
      *permissions);
}

//  bool QResourceFileEngine::close()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QResourceFileEngine5closeEv(QResourceFileEngine *self) {
  return self->close();
}

//  bool QResourceFileEngine::flush()
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QResourceFileEngine5flushEv(QResourceFileEngine *self) {
  return self->flush();
}

//  qint64 QResourceFileEngine::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QResourceFileEngine4sizeEv(
    const QResourceFileEngine *self) {
  return self->size();
}

//  qint64 QResourceFileEngine::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK19QResourceFileEngine3posEv(
    const QResourceFileEngine *self) {
  return self->pos();
}

//  bool QResourceFileEngine::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QResourceFileEngine5atEndEv(
    const QResourceFileEngine *self) {
  return self->atEnd();
}

//  bool QResourceFileEngine::seek(qint64 a0)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QResourceFileEngine4seekEx(
    QResourceFileEngine *self,
    qint64 a0) {
  return self->seek(a0);
}

//  qint64 QResourceFileEngine::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_ZN19QResourceFileEngine4readEPcx(
    QResourceFileEngine *self,
    char *data,
    qint64 maxlen) {
  return self->read(data, maxlen);
}

//  bool QResourceFileEngine::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QResourceFileEngine13caseSensitiveEv(
    const QResourceFileEngine *self) {
  return self->caseSensitive();
}

//  FileFlags QResourceFileEngine::fileFlags(FileFlags type) const
extern "C" Q_DECL_EXPORT
int ritual_ZNK19QResourceFileEngine9fileFlagsE6QFlagsIN19QAbstractFileEngine8FileFlagEE(
    const QResourceFileEngine *self,
    int type) {
  return static_cast<int>(
      self->fileFlags(
          QFlags<QAbstractFileEngine::FileFlag>::fromInt(type)).toInt());
}

//  QString QResourceFileEngine::fileName(QAbstractFileEngine::FileName file)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK19QResourceFileEngine8fileNameEN19QAbstractFileEngine8FileNameE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::FileName file) {
  return new QString(self->fileName(file));
}

//  uint QResourceFileEngine::ownerId(FileOwner a0) const
extern "C" Q_DECL_EXPORT
uint ritual_ZNK19QResourceFileEngine7ownerIdEN19QAbstractFileEngine9FileOwnerE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return self->ownerId(a0);
}

//  QDateTime QResourceFileEngine::fileTime(QFile::FileTime time) const
extern "C" Q_DECL_EXPORT
QDateTime *ritual_ZNK19QResourceFileEngine8fileTimeEN11QFileDevice8FileTimeE(
    const QResourceFileEngine *self,
    const QFile::FileTime *time) {
  return new QDateTime(self->fileTime(*time));
}

//  IteratorUniquePtr QResourceFileEngine::beginEntryList(const QString
//      &path, QDirListing::IteratorFlags filters, const QStringList
//      &filterNames)
extern "C" Q_DECL_EXPORT
QAbstractFileEngine::IteratorUniquePtr *ritual_ZN19QResourceFileEngine14beginEntryListERK7QString6QFlagsIN11QDirListing12IteratorFlagEERK5QListIS0_E(
    QResourceFileEngine *self,
    const QString *path,
    int filters,
    const QList<QString> *filterNames) {
  return new QAbstractFileEngine::IteratorUniquePtr(
      self->beginEntryList(
          *path,
          QFlags<QDirListing::IteratorFlag>::fromInt(filters),
          *filterNames));
}

//  bool QResourceFileEngine::extension(Extension extension, const
//      ExtensionOption *option, ExtensionReturn *output)
extern "C" Q_DECL_EXPORT
bool ritual_ZN19QResourceFileEngine9extensionEN19QAbstractFileEngine9ExtensionEPKNS0_15ExtensionOptionEPNS0_15ExtensionReturnE(
    QResourceFileEngine *self,
    QAbstractFileEngine::Extension extension,
    const QAbstractFileEngine::ExtensionOption *option,
    QAbstractFileEngine::ExtensionReturn *output) {
  return self->extension(extension, option, output);
}

//  bool QResourceFileEngine::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QResourceFileEngine17supportsExtensionEN19QAbstractFileEngine9ExtensionE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::Extension extension) {
  return self->supportsExtension(extension);
}

//  a Python function taken by a CuteQResourceFileEngine, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QResourceFileEngine(
    QResourceFileEngine *self,
    const char *key,
    void *call) {
  return static_cast<CuteQResourceFileEngine *>(self)->take(key, call);
}

#if !defined(QT_BOOTSTRAPPED)
//  void QResourceFileEngine::setFileName(const QString &file)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QResourceFileEngine11setFileNameERK7QString(
    QResourceFileEngine *self,
    const QString *file) {
  self->QResourceFileEngine::setFileName(*file);
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  bool QResourceFileEngine::close()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QResourceFileEngine5closeEv(QResourceFileEngine *self) {
  return self->QResourceFileEngine::close();
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  bool QResourceFileEngine::flush()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QResourceFileEngine5flushEv(QResourceFileEngine *self) {
  return self->QResourceFileEngine::flush();
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  qint64 QResourceFileEngine::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK19QResourceFileEngine4sizeEv(
    const QResourceFileEngine *self) {
  return self->QResourceFileEngine::size();
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  qint64 QResourceFileEngine::pos() const
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZNK19QResourceFileEngine3posEv(
    const QResourceFileEngine *self) {
  return self->QResourceFileEngine::pos();
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  bool QResourceFileEngine::atEnd() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QResourceFileEngine5atEndEv(
    const QResourceFileEngine *self) {
  return self->QResourceFileEngine::atEnd();
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  bool QResourceFileEngine::seek(qint64 a0)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN19QResourceFileEngine4seekEx(
    QResourceFileEngine *self,
    qint64 a0) {
  return self->QResourceFileEngine::seek(a0);
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  qint64 QResourceFileEngine::read(char *data, qint64 maxlen)
extern "C" Q_DECL_EXPORT
qint64 ritual_own_ZN19QResourceFileEngine4readEPcx(
    QResourceFileEngine *self,
    char *data,
    qint64 maxlen) {
  return self->QResourceFileEngine::read(data, maxlen);
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  bool QResourceFileEngine::caseSensitive() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QResourceFileEngine13caseSensitiveEv(
    const QResourceFileEngine *self) {
  return self->QResourceFileEngine::caseSensitive();
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  FileFlags QResourceFileEngine::fileFlags(FileFlags type) const
extern "C" Q_DECL_EXPORT
int ritual_own_ZNK19QResourceFileEngine9fileFlagsE6QFlagsIN19QAbstractFileEngine8FileFlagEE(
    const QResourceFileEngine *self,
    int type) {
  return static_cast<int>(
      self->QResourceFileEngine::fileFlags(
          QFlags<QAbstractFileEngine::FileFlag>::fromInt(type)).toInt());
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  QString QResourceFileEngine::fileName(QAbstractFileEngine::FileName file)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK19QResourceFileEngine8fileNameEN19QAbstractFileEngine8FileNameE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::FileName file) {
  return new QString(self->QResourceFileEngine::fileName(file));
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  uint QResourceFileEngine::ownerId(FileOwner a0) const
extern "C" Q_DECL_EXPORT
uint ritual_own_ZNK19QResourceFileEngine7ownerIdEN19QAbstractFileEngine9FileOwnerE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::FileOwner a0) {
  return self->QResourceFileEngine::ownerId(a0);
}
#endif  // !defined(QT_BOOTSTRAPPED)

#if !defined(QT_BOOTSTRAPPED)
//  bool QResourceFileEngine::supportsExtension(Extension extension) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK19QResourceFileEngine17supportsExtensionEN19QAbstractFileEngine9ExtensionE(
    const QResourceFileEngine *self,
    QAbstractFileEngine::Extension extension) {
  return self->QResourceFileEngine::supportsExtension(extension);
}
#endif  // !defined(QT_BOOTSTRAPPED)

//  a QAbstractFileEngine::IteratorUniquePtr a ritual of QResourceFileEngine
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QResourceFileEngine__QAbstractFileEngine_IteratorUniquePtr(
    QAbstractFileEngine::IteratorUniquePtr *self) {
  delete self;
}
