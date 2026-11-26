//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qsettings_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(settings)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qsettings_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <optional>
#include <QtCore/QVariant>
#include <QtCore/QString>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsettings.h>
#include <QtCore/private/qsettings_p.h>
#include <QtCore/qcache.h>
#include <QtCore/qcoreapplication.h>
#include <QtCore/qdatastream.h>
#include <QtCore/qdir.h>
#include <QtCore/qfile.h>
#include <QtCore/qfileinfo.h>
#include <QtCore/qlibraryinfo.h>
#include <QtCore/private/qlocking_p.h>
#include <QtCore/qmutex.h>
#include <QtCore/qpoint.h>
#include <QtCore/qrect.h>
#include <QtCore/qsize.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/private/qstringconverter_p.h>
#include <QtCore/qtemporaryfile.h>
#include <QtCore/private/qtools_p.h>
#ifndef QT_BOOTSTRAPPED
#include <QtCore/qsavefile.h>
#include <QtCore/qlockfile.h>
#endif
#ifdef Q_OS_VXWORKS
#  include <ioLib.h>
#endif
#include <algorithm>
#include <stdlib.h>
#ifdef Q_OS_WIN
#  include <QtCore/qt_windows.h>
#  include <shlobj.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qsettings.cpp, line 75, as local:qsettings.cpp:ConfFileHash
typedef QHash<QString, QConfFile *> ConfFileHash;

//  from src/corelib/io/qsettings.cpp, line 76, as local:qsettings.cpp:ConfFileCache
typedef QCache<QString, QConfFile> ConfFileCache;

//  from src/corelib/io/qsettings.cpp, line 78, as local:qsettings.cpp:Path
namespace {
struct Path
    {
        // Note: Defining constructors explicitly because of buggy C++11
        // implementation in MSVC (uniform initialization).
        Path() {}
        Path(const QString & p, bool ud) : path(p), userDefined(ud) {}
        QString path;
        bool userDefined = false; //!< true - user defined, overridden by setPath
    };
}  // namespace

//  from src/corelib/io/qsettings.cpp, line 178, as _ZN16QSettingsPrivateC2EN9QSettings6FormatE
inline QSettingsPrivate::QSettingsPrivate(QSettings::Format format)
    : format(format), scope(QSettings::UserScope /* nothing better to put */), fallbacks(true),
      pendingChanges(false), status(QSettings::NoError)
{
}

//  from src/corelib/io/qsettings.cpp, line 191, as _ZN16QSettingsPrivateD2Ev
inline QSettingsPrivate::~QSettingsPrivate()
{
}

//  from src/corelib/io/qsettings.cpp, line 906, as _ZN24QConfFileSettingsPrivate10initAccessEv
#if defined(Q_OS_LINUX)
inline void QConfFileSettingsPrivate::initAccess()
{
    if (!confFiles.isEmpty()) {
#if defined Q_OS_WASM
        if (format > QSettings::IniFormat && format != QSettings::WebIndexedDBFormat) {
#else
        if (format > QSettings::IniFormat) {
#endif
            if (!readFunc)
                setStatus(QSettings::AccessError);
        }
    }

    sync();       // loads the files the first time
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qsettings.cpp, line 1194, as _ZN24QConfFileSettingsPrivate3setERK7QStringRK8QVariant
inline void QConfFileSettingsPrivate::set(const QString &key, const QVariant &value)
{
    if (confFiles.isEmpty())
        return;

    // Note: First config file is always the most specific.
    QConfFile *confFile = confFiles.at(0);

    QSettingsKey theKey(key, caseSensitivity, nextPosition++);
    const auto locker = qt_scoped_lock(confFile->mutex);
    confFile->removedKeys.remove(theKey);
    confFile->addedKeys.insert(theKey, value);
}

//  from src/corelib/io/qsettings.cpp, line 1289, as _ZN24QConfFileSettingsPrivate4syncEv
inline void QConfFileSettingsPrivate::sync()
{
    // people probably won't be checking the status a whole lot, so in case of
    // error we just try to go on and make the best of it

    for (auto confFile : std::as_const(confFiles)) {
        const auto locker = qt_scoped_lock(confFile->mutex);
        syncConfFile(confFile);
    }
}

//  from src/corelib/io/qsettings.cpp, line 1275, as _ZN24QConfFileSettingsPrivate5clearEv
inline void QConfFileSettingsPrivate::clear()
{
    if (confFiles.isEmpty())
        return;

    // Note: First config file is always the most specific.
    QConfFile *confFile = confFiles.at(0);

    const auto locker = qt_scoped_lock(confFile->mutex);
    ensureAllSectionsParsed(confFile);
    confFile->addedKeys.clear();
    confFile->removedKeys = confFile->originalKeys;
}

//  from src/corelib/io/qsettings.cpp, line 1300, as _ZN24QConfFileSettingsPrivate5flushEv
inline void QConfFileSettingsPrivate::flush()
{
    sync();
}

//  from src/corelib/io/qsettings.cpp, line 1165, as _ZN24QConfFileSettingsPrivate6removeERK7QString
inline void QConfFileSettingsPrivate::remove(const QString &key)
{
    if (confFiles.isEmpty())
        return;

    // Note: First config file is always the most specific.
    QConfFile *confFile = confFiles.at(0);

    QSettingsKey theKey(key, caseSensitivity);
    QSettingsKey prefix(key + u'/', caseSensitivity);
    const auto locker = qt_scoped_lock(confFile->mutex);

    ensureSectionParsed(confFile, theKey);
    ensureSectionParsed(confFile, prefix);

    auto i = confFile->addedKeys.lowerBound(prefix);
    while (i != confFile->addedKeys.end() && i.key().startsWith(prefix))
        i = confFile->addedKeys.erase(i);
    confFile->addedKeys.remove(theKey);

    auto j = const_cast<const ParsedSettingsMap *>(&confFile->originalKeys)->lowerBound(prefix);
    while (j != confFile->originalKeys.constEnd() && j.key().startsWith(prefix)) {
        confFile->removedKeys.insert(j.key(), QVariant());
        ++j;
    }
    if (confFile->originalKeys.contains(theKey))
        confFile->removedKeys.insert(theKey, QVariant());
}

//  from src/corelib/io/qsettings.cpp, line 1314, as _ZNK24QConfFileSettingsPrivate10isWritableEv
#if defined(Q_OS_LINUX)
inline bool QConfFileSettingsPrivate::isWritable() const
{
#if defined(Q_OS_WASM)
    if (format > QSettings::IniFormat && format != QSettings::WebIndexedDBFormat && !writeFunc)
#else
    if (format > QSettings::IniFormat && !writeFunc)
#endif
        return false;

    if (confFiles.isEmpty())
        return false;

    return confFiles.at(0)->isWritable();
}
#endif  // defined(Q_OS_LINUX)

//  from src/corelib/io/qsettings.cpp, line 1208, as _ZNK24QConfFileSettingsPrivate3getERK7QString
inline std::optional<QVariant> QConfFileSettingsPrivate::get(const QString &key) const
{
    QSettingsKey theKey(key, caseSensitivity);
    ParsedSettingsMap::const_iterator j;
    bool found = false;

    for (auto confFile : std::as_const(confFiles)) {
        const auto locker = qt_scoped_lock(confFile->mutex);

        if (!confFile->addedKeys.isEmpty()) {
            j = confFile->addedKeys.constFind(theKey);
            found = (j != confFile->addedKeys.constEnd());
        }
        if (!found) {
            ensureSectionParsed(confFile, theKey);
            j = confFile->originalKeys.constFind(theKey);
            found = (j != confFile->originalKeys.constEnd()
                     && !confFile->removedKeys.contains(theKey));
        }

        if (found)
            return *j;
        if (!fallbacks)
            break;
    }
    return std::nullopt;
}

//  from src/corelib/io/qsettings.cpp, line 1236, as _ZNK24QConfFileSettingsPrivate8childrenERK7QStringN16QSettingsPrivate9ChildSpecE
inline QStringList QConfFileSettingsPrivate::children(const QString &prefix, ChildSpec spec) const
{
    QStringList result;

    QSettingsKey thePrefix(prefix, caseSensitivity);
    qsizetype startPos = prefix.size();

    for (auto confFile : std::as_const(confFiles)) {
        const auto locker = qt_scoped_lock(confFile->mutex);

        if (thePrefix.isEmpty())
            ensureAllSectionsParsed(confFile);
        else
            ensureSectionParsed(confFile, thePrefix);

        const auto &originalKeys = confFile->originalKeys;
        auto i = originalKeys.lowerBound(thePrefix);
        while (i != originalKeys.end() && i.key().startsWith(thePrefix)) {
            if (!confFile->removedKeys.contains(i.key()))
                processChild(QStringView{i.key().originalCaseKey()}.sliced(startPos), spec, result);
            ++i;
        }

        const auto &addedKeys = confFile->addedKeys;
        auto j = addedKeys.lowerBound(thePrefix);
        while (j != addedKeys.end() && j.key().startsWith(thePrefix)) {
            processChild(QStringView{j.key().originalCaseKey()}.sliced(startPos), spec, result);
            ++j;
        }

        if (!fallbacks)
            break;
    }
    std::sort(result.begin(), result.end());
    result.erase(std::unique(result.begin(), result.end()),
                 result.end());
    return result;
}

//  from src/corelib/io/qsettings.cpp, line 1305, as _ZNK24QConfFileSettingsPrivate8fileNameEv
inline QString QConfFileSettingsPrivate::fileName() const
{
    if (confFiles.isEmpty())
        return QString();

    // Note: First config file is always the most specific.
    return confFiles.at(0)->name;
}

//  from src/corelib/io/qsettings.cpp, line 526, as _ZN16QSettingsPrivate15iniUnescapedKeyE14QByteArrayViewR7QString
inline bool QSettingsPrivate::iniUnescapedKey(QByteArrayView key, QString &result)
{
    const QString decoded = QString::fromUtf8(key);
    const qsizetype size = decoded.size();
    result.reserve(result.size() + size);
    qsizetype i = 0;
    bool lowercaseOnly = true;
    while (i < size) {
        char16_t ch = decoded.at(i).unicode();

        if (ch == '\\') {
            result += u'/';
            ++i;
            continue;
        }

        if (ch != '%' || i == size - 1) {
            QChar qch(ch);
            if (qch.isUpper())
                lowercaseOnly = false;
            result += qch;
            ++i;
            continue;
        }

        int numDigits = 2;
        qsizetype firstDigitPos = i + 1;

        ch = decoded.at(i + 1).unicode();
        if (ch == 'U') {
            ++firstDigitPos;
            numDigits = 4;
        }

        if (firstDigitPos + numDigits > size) {
            result += u'%';
            ++i;
            continue;
        }

        bool ok;
        ch = QStringView(decoded).sliced(firstDigitPos, numDigits).toUShort(&ok, 16);
        if (!ok) {
            result += u'%';
            ++i;
            continue;
        }

        QChar qch(ch);
        if (qch.isUpper())
            lowercaseOnly = false;
        result += qch;
        i = firstDigitPos + numDigits;
    }
    return lowercaseOnly;
}

//  from src/corelib/io/qsettings.cpp, line 447, as _ZN16QSettingsPrivate15stringToVariantERK7QString
inline QVariant QSettingsPrivate::stringToVariant(const QString &s)
{
    if (s.startsWith(u'@')) {
        if (s.endsWith(u')')) {
            if (s.startsWith("@ByteArray("_L1)) {
                return QVariant(QStringView{s}.sliced(11).chopped(1).toLatin1());
            } else if (s.startsWith("@String("_L1)) {
                return QVariant(QStringView{s}.sliced(8).chopped(1).toString());
            } else if (s.startsWith("@Variant("_L1)
                       || s.startsWith("@DateTime("_L1)) {
#ifndef QT_NO_DATASTREAM
                QDataStream::Version version;
                int offset;
                if (s.at(1) == u'D') {
                    version = QDataStream::Qt_5_6;
                    offset = 10;
                } else {
                    version = QDataStream::Qt_4_0;
                    offset = 9;
                }
                QByteArray a = QStringView{s}.sliced(offset).toLatin1();
                QDataStream stream(&a, QIODevice::ReadOnly);
                stream.setVersion(version);
                QVariant result;
                stream >> result;
                return result;
#else
                Q_ASSERT(!"QSettings: Cannot load custom types without QDataStream support");
#endif
            } else if (s.startsWith("@Rect("_L1)) {
                QStringList args = QSettingsPrivate::splitArgs(s, 5);
                if (args.size() == 4)
                    return QVariant(QRect(args[0].toInt(), args[1].toInt(), args[2].toInt(), args[3].toInt()));
            } else if (s.startsWith("@Size("_L1)) {
                QStringList args = QSettingsPrivate::splitArgs(s, 5);
                if (args.size() == 2)
                    return QVariant(QSize(args[0].toInt(), args[1].toInt()));
            } else if (s.startsWith("@Point("_L1)) {
                QStringList args = QSettingsPrivate::splitArgs(s, 6);
                if (args.size() == 2)
                    return QVariant(QPoint(args[0].toInt(), args[1].toInt()));
            } else if (s == "@Invalid()"_L1) {
                return QVariant();
            }

        }
        if (s.startsWith("@@"_L1))
            return QVariant(s.sliced(1));
    }

    return QVariant(s);
}

//  from src/corelib/io/qsettings.cpp, line 346, as _ZN16QSettingsPrivate23stringListToVariantListERK5QListI7QStringE
inline QVariant QSettingsPrivate::stringListToVariantList(const QStringList &l)
{
    QStringList outStringList = l;
    for (qsizetype i = 0; i < outStringList.size(); ++i) {
        const QString &str = outStringList.at(i);

        if (str.startsWith(u'@')) {
            if (str.size() < 2 || str.at(1) != u'@') {
                QVariantList variantList;
                variantList.reserve(l.size());
                for (const auto &s : l)
                    variantList.append(stringToVariant(s));
                return variantList;
            }
            outStringList[i].remove(0, 1);
        }
    }
    return outStringList;
}

//  from src/corelib/io/qsettings.cpp, line 312, as _ZNK16QSettingsPrivate9setStatusEN9QSettings6StatusE
inline void QSettingsPrivate::setStatus(QSettings::Status status) const
{
    if (status == QSettings::NoError || this->status == QSettings::NoError)
        this->status = status;
}

//  from src/corelib/io/qsettings.cpp, line 123, as _ZNK9QConfFile10isWritableEv
inline bool QConfFile::isWritable() const
{
    QFileInfo fileInfo(name);

#if QT_CONFIG(temporaryfile)
    if (fileInfo.exists()) {
#endif
        QFile file(name);
        return file.open(QFile::ReadWrite);
#if QT_CONFIG(temporaryfile)
    } else {
        // Create the directories to the file.
        QDir dir(fileInfo.absolutePath());
        if (!dir.exists()) {
            if (!dir.mkpath(dir.absolutePath()))
                return false;
        }

        // we use a temporary file to avoid race conditions
        QTemporaryFile file(name);
        return file.open();
    }
#endif
}

//  from src/corelib/io/qsettings.cpp, line 112, as _ZNK9QConfFile12mergedKeyMapEv
inline ParsedSettingsMap QConfFile::mergedKeyMap() const
{
    ParsedSettingsMap result = originalKeys;

    for (auto i = removedKeys.begin(); i != removedKeys.end(); ++i)
        result.remove(i.key());
    for (auto i = addedKeys.begin(); i != addedKeys.end(); ++i)
        result.insert(i.key(), i.value());
    return result;
}
//  -----------------------------------------------------------------------

//  A QConfFileSettingsPrivate that Python can take functions over in. Every QConfFileSettingsPrivate
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQConfFileSettingsPrivateCall0)(const void *, const QString *, int *);
typedef void (*CuteQConfFileSettingsPrivateCall1)(const void *, const QString *, const QVariant *, int *);
typedef void (*CuteQConfFileSettingsPrivateCall2)(const void *, int *);
typedef void (*CuteQConfFileSettingsPrivateCall3)(const void *, int *);
typedef void (*CuteQConfFileSettingsPrivateCall4)(const void *, int *);
typedef bool (*CuteQConfFileSettingsPrivateCall5)(const void *, int *);
typedef QString * (*CuteQConfFileSettingsPrivateCall6)(const void *, int *);
typedef void (*CuteQConfFileSettingsPrivateCall7)(const void *, int *);
class CuteQConfFileSettingsPrivate : public QConfFileSettingsPrivate {
public:
  using QConfFileSettingsPrivate::QConfFileSettingsPrivate;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSettingsPrivate6removeERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate3setERK7QStringRK8QVariant")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate5clearEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate4syncEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSettingsPrivate5flushEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSettingsPrivate10isWritableEv")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSettingsPrivate8fileNameEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN24QConfFileSettingsPrivate10initAccessEv")) {
      taken[7] = call;
      return true;
    }
    return false;
  }

  //  void QConfFileSettingsPrivate::remove(const QString &key)
  void remove(const QString &key) override {
    if (taken[0]) {
      int handled = 0;
      CuteQConfFileSettingsPrivateCall0 call = reinterpret_cast<CuteQConfFileSettingsPrivateCall0>(taken[0]);
      call(this, &key, &handled);
      if (handled) return;
    }
    QConfFileSettingsPrivate::remove(key);
  }

  //  void QConfFileSettingsPrivate::set(const QString &key, const QVariant
  //      &value)
  void set(const QString &key, const QVariant &value) override {
    if (taken[1]) {
      int handled = 0;
      CuteQConfFileSettingsPrivateCall1 call = reinterpret_cast<CuteQConfFileSettingsPrivateCall1>(taken[1]);
      call(this, &key, &value, &handled);
      if (handled) return;
    }
    QConfFileSettingsPrivate::set(key, value);
  }

  //  void QConfFileSettingsPrivate::clear()
  void clear() override {
    if (taken[2]) {
      int handled = 0;
      CuteQConfFileSettingsPrivateCall2 call = reinterpret_cast<CuteQConfFileSettingsPrivateCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QConfFileSettingsPrivate::clear();
  }

  //  void QConfFileSettingsPrivate::sync()
  void sync() override {
    if (taken[3]) {
      int handled = 0;
      CuteQConfFileSettingsPrivateCall3 call = reinterpret_cast<CuteQConfFileSettingsPrivateCall3>(taken[3]);
      call(this, &handled);
      if (handled) return;
    }
    QConfFileSettingsPrivate::sync();
  }

  //  void QConfFileSettingsPrivate::flush()
  void flush() override {
    if (taken[4]) {
      int handled = 0;
      CuteQConfFileSettingsPrivateCall4 call = reinterpret_cast<CuteQConfFileSettingsPrivateCall4>(taken[4]);
      call(this, &handled);
      if (handled) return;
    }
    QConfFileSettingsPrivate::flush();
  }

  //  bool QConfFileSettingsPrivate::isWritable() const
  bool isWritable() const override {
    if (taken[5]) {
      int handled = 0;
      CuteQConfFileSettingsPrivateCall5 call = reinterpret_cast<CuteQConfFileSettingsPrivateCall5>(taken[5]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QConfFileSettingsPrivate::isWritable();
  }

  //  QString QConfFileSettingsPrivate::fileName() const
  QString fileName() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQConfFileSettingsPrivateCall6 call = reinterpret_cast<CuteQConfFileSettingsPrivateCall6>(taken[6]);
      QString * given = call(this, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return QConfFileSettingsPrivate::fileName();
  }

  //  void QConfFileSettingsPrivate::initAccess()
  void initAccess() override {
    if (taken[7]) {
      int handled = 0;
      CuteQConfFileSettingsPrivateCall7 call = reinterpret_cast<CuteQConfFileSettingsPrivateCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QConfFileSettingsPrivate::initAccess();
  }
};

//  void QConfFileSettingsPrivate::remove(const QString &key)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QConfFileSettingsPrivate6removeERK7QString(
    QConfFileSettingsPrivate *self,
    const QString *key) {
  self->remove(*key);
}

//  void QConfFileSettingsPrivate::set(const QString &key, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QConfFileSettingsPrivate3setERK7QStringRK8QVariant(
    QConfFileSettingsPrivate *self,
    const QString *key,
    const QVariant *value) {
  self->set(*key, *value);
}

//  std::optional<QVariant> QConfFileSettingsPrivate::get(const QString &key)
//      const
extern "C" Q_DECL_EXPORT
std::optional<QVariant> *ritual_ZNK24QConfFileSettingsPrivate3getERK7QString(
    const QConfFileSettingsPrivate *self,
    const QString *key) {
  return new std::optional<QVariant>(self->get(*key));
}

//  QStringList QConfFileSettingsPrivate::children(const QString &prefix,
//      ChildSpec spec) const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK24QConfFileSettingsPrivate8childrenERK7QStringN16QSettingsPrivate9ChildSpecE(
    const QConfFileSettingsPrivate *self,
    const QString *prefix,
    QSettingsPrivate::ChildSpec spec) {
  return new QList<QString>(self->children(*prefix, spec));
}

//  void QConfFileSettingsPrivate::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QConfFileSettingsPrivate5clearEv(
    QConfFileSettingsPrivate *self) {
  self->clear();
}

//  void QConfFileSettingsPrivate::sync()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QConfFileSettingsPrivate4syncEv(
    QConfFileSettingsPrivate *self) {
  self->sync();
}

//  void QConfFileSettingsPrivate::flush()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QConfFileSettingsPrivate5flushEv(
    QConfFileSettingsPrivate *self) {
  self->flush();
}

//  bool QConfFileSettingsPrivate::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK24QConfFileSettingsPrivate10isWritableEv(
    const QConfFileSettingsPrivate *self) {
  return self->isWritable();
}

//  QString QConfFileSettingsPrivate::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK24QConfFileSettingsPrivate8fileNameEv(
    const QConfFileSettingsPrivate *self) {
  return new QString(self->fileName());
}

//  const QList<QConfFile *> &QConfFileSettingsPrivate::getConfFiles() const
extern "C" Q_DECL_EXPORT
QList<QConfFile *> *ritual_ZNK24QConfFileSettingsPrivate12getConfFilesEv(
    const QConfFileSettingsPrivate *self) {
  return new QList<QConfFile *>(self->getConfFiles());
}

//  void QConfFileSettingsPrivate::initAccess()
extern "C" Q_DECL_EXPORT
void ritual_ZN24QConfFileSettingsPrivate10initAccessEv(
    QConfFileSettingsPrivate *self) {
  self->initAccess();
}

//  a Python function taken by a CuteQConfFileSettingsPrivate, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QConfFileSettingsPrivate(
    QConfFileSettingsPrivate *self,
    const char *key,
    void *call) {
  return static_cast<CuteQConfFileSettingsPrivate *>(self)->take(key, call);
}

//  void QConfFileSettingsPrivate::set(const QString &key, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QConfFileSettingsPrivate3setERK7QStringRK8QVariant(
    QConfFileSettingsPrivate *self,
    const QString *key,
    const QVariant *value) {
  self->QConfFileSettingsPrivate::set(*key, *value);
}

//  void QConfFileSettingsPrivate::flush()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QConfFileSettingsPrivate5flushEv(
    QConfFileSettingsPrivate *self) {
  self->QConfFileSettingsPrivate::flush();
}

#if defined(Q_OS_LINUX)
//  bool QConfFileSettingsPrivate::isWritable() const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK24QConfFileSettingsPrivate10isWritableEv(
    const QConfFileSettingsPrivate *self) {
  return self->QConfFileSettingsPrivate::isWritable();
}
#endif  // defined(Q_OS_LINUX)

//  QString QConfFileSettingsPrivate::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_own_ZNK24QConfFileSettingsPrivate8fileNameEv(
    const QConfFileSettingsPrivate *self) {
  return new QString(self->QConfFileSettingsPrivate::fileName());
}

#if defined(Q_OS_LINUX)
//  void QConfFileSettingsPrivate::initAccess()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QConfFileSettingsPrivate10initAccessEv(
    QConfFileSettingsPrivate *self) {
  self->QConfFileSettingsPrivate::initAccess();
}
#endif  // defined(Q_OS_LINUX)

//  a std::optional<QVariant> a ritual of QConfFileSettingsPrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QConfFileSettingsPrivate__std_optional_QVariant(
    std::optional<QVariant> *self) {
  delete self;
}

#endif  // QT_CONFIG(settings)
