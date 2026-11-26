//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimedatabase_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimedatabase_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <qplatformdefs.h> // always first
#include <QtCore/qmimedatabase.h>
#include <QtCore/private/qmimedatabase_p.h>
#include <QtCore/private/qmimeprovider_p.h>
#include <QtCore/private/qmimetype_p.h>
#include <QtCore/private/qduplicatetracker_p.h>
#include <QtCore/private/qfilesystementry_p.h>
#include <QtCore/QFile>
#include <QtCore/QFileInfo>
#include <QtCore/QStandardPaths>
#include <QtCore/QBuffer>
#include <QtCore/QUrl>
#include <QtCore/QDebug>
#include <algorithm>
#include <functional>
#include <stack>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/io/qfilesystementry.cpp, line 21, as local:qfilesystementry.cpp:Uninitialized
constexpr int Uninitialized = -2;

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 32, as local:qmimedatabase.cpp:directoryMimeType
static QString directoryMimeType()
{
    return QStringLiteral("inode/directory");
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 36, as local:qmimedatabase.cpp:plainTextMimeType
static QString plainTextMimeType()
{
    return QStringLiteral("text/plain");
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 57, as local:qmimedatabase.cpp:qmime_secondsBetweenChecks
Q_CONSTINIT
#ifdef QT_BUILD_INTERNAL
Q_CORE_EXPORT
#else
static const
#endif
int qmime_secondsBetweenChecks = 5;

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 73, as local:qmimedatabase.cpp:locateMimeDirectories
static QStringList locateMimeDirectories()
{
    QStringList dirs =
            QStandardPaths::locateAll(QStandardPaths::GenericDataLocation, QStringLiteral("mime"),
                                      QStandardPaths::LocateDirectory);
    dirs.append(u":/qt-project.org/qmime"_s);
    return dirs;
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 327, as local:qmimedatabase.cpp:isTextFile
static inline bool isTextFile(const QByteArray &data)
{
    // UTF16 byte order marks
    static const char bigEndianBOM[] = "\xFE\xFF";
    static const char littleEndianBOM[] = "\xFF\xFE";
    if (data.startsWith(bigEndianBOM) || data.startsWith(littleEndianBOM))
        return true;

    // Check the first 128 bytes (see shared-mime spec)
    const char *p = data.constData();
    const char *e = p + qMin(128, data.size());
    for ( ; p < e; ++p) {
        if (static_cast<unsigned char>(*p) < 32 && *p != 9 && *p !=10 && *p != 13)
            return false;
    }

    return true;
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 287, as _ZN20QMimeDatabasePrivate7parentsERK7QString
inline QStringList QMimeDatabasePrivate::parents(const QString &mimeName)
{
#if QT_CONFIG(thread) // stub implementation always returns true
    Q_ASSERT(!mutex.tryLock());
#endif
    QStringList result;
    for (const auto &provider : providers())
        provider->addParents(mimeName, result);

    // Implicit rule from the spec: all text/* types are subclasses of text/plain. It holds even
    // for types that declare other parents, and shared-mime-info >= 2.5 relies on that rather
    // than listing text/plain (e.g. text/x-shellscript only declares application/x-executable).
    if (mimeName.startsWith("text/"_L1) && mimeName != plainTextMimeType()
        && !result.contains(plainTextMimeType())) {
        result.append(plainTextMimeType());
    }

    if (result.isEmpty()) {
        const QString parent = fallbackParent(mimeName);
        if (!parent.isEmpty())
            result.append(parent);
    }
    return result;
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 159, as _ZN20QMimeDatabasePrivate9providersEv
inline const QMimeDatabasePrivate::Providers &QMimeDatabasePrivate::providers()
{
#if QT_CONFIG(thread) // stub implementation always returns true
    Q_ASSERT(!mutex.tryLock()); // caller should have locked mutex
#endif
    if (m_providers.empty()) {
        loadProviders();
        m_lastCheck.start();
    } else {
        if (shouldCheck())
            loadProviders();
    }
    return m_providers;
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 86, as _ZN20QMimeDatabasePrivate13loadProvidersEv
inline void QMimeDatabasePrivate::loadProviders()
{
    // We use QStandardPaths every time to check if new files appeared
    const QStringList mimeDirs = locateMimeDirectories();
    const auto fdoIterator = std::find_if(mimeDirs.constBegin(), mimeDirs.constEnd(), [](const QString &mimeDir) -> bool {
        return QFileInfo::exists(mimeDir + "/packages/freedesktop.org.xml"_L1); }
    );
    const bool needInternalDB = QMimeXMLProvider::InternalDatabaseAvailable && fdoIterator == mimeDirs.constEnd();
    //qDebug() << "mime dirs:" << mimeDirs;

    Providers currentProviders;
    std::swap(m_providers, currentProviders);

    m_providers.reserve(mimeDirs.size() + (needInternalDB ? 1 : 0));

    for (const QString &mimeDir : mimeDirs) {
        const QString cacheFile = mimeDir + "/mime.cache"_L1;
        // Check if we already have a provider for this dir
        const auto predicate = [mimeDir](const std::unique_ptr<QMimeProviderBase> &prov)
        {
            return prov && prov->directory() == mimeDir;
        };
        const auto it = std::find_if(currentProviders.begin(), currentProviders.end(), predicate);
        if (it == currentProviders.end()) {
            std::unique_ptr<QMimeProviderBase> provider;
#if defined(QT_USE_MMAP)
            if (qEnvironmentVariableIsEmpty("QT_NO_MIME_CACHE") && QFileInfo::exists(cacheFile)) {
                provider.reset(new QMimeBinaryProvider(this, mimeDir));
                //qDebug() << "Created binary provider for" << mimeDir;
                if (!provider->isValid()) {
                    provider.reset();
                }
            }
#endif
            if (!provider) {
                provider.reset(new QMimeXMLProvider(this, mimeDir));
                //qDebug() << "Created XML provider for" << mimeDir;
            }
            m_providers.push_back(std::move(provider));
        } else {
            auto provider = std::move(*it); // take provider out of the vector
            provider->ensureLoaded();
            if (!provider->isValid()) {
                provider.reset(new QMimeXMLProvider(this, mimeDir));
                //qDebug() << "Created XML provider to replace binary provider for" << mimeDir;
            }
            m_providers.push_back(std::move(provider));
        }
    }
    // mimeDirs is sorted "most local first, most global last"
    // so the internal XML DB goes at the end
    if (needInternalDB) {
        // Check if we already have a provider for the InternalDatabase
        const auto isInternal = [](const std::unique_ptr<QMimeProviderBase> &prov)
        {
            return prov && prov->isInternalDatabase();
        };
        const auto it = std::find_if(currentProviders.begin(), currentProviders.end(), isInternal);
        if (it == currentProviders.end()) {
            m_providers.push_back(Providers::value_type(new QMimeXMLProvider(this, QMimeXMLProvider::InternalDatabase)));
        } else {
            m_providers.push_back(std::move(*it));
        }
    }

    auto it = m_providers.begin();
    (*it)->setOverrideProvider(nullptr);
    ++it;
    const auto end = m_providers.end();
    for (; it != end; ++it)
        (*it)->setOverrideProvider((it - 1)->get());
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 48, as _ZN20QMimeDatabasePrivateC1Ev
inline QMimeDatabasePrivate::QMimeDatabasePrivate()
    : m_defaultMimeType(QStringLiteral("application/octet-stream"))
{
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 53, as _ZN20QMimeDatabasePrivateD1Ev
inline QMimeDatabasePrivate::~QMimeDatabasePrivate()
{
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 65, as _ZN20QMimeDatabasePrivate11shouldCheckEv
inline bool QMimeDatabasePrivate::shouldCheck()
{
    if (m_lastCheck.isValid() && m_lastCheck.elapsed() < qmime_secondsBetweenChecks * 1000)
        return false;
    m_lastCheck.start();
    return true;
}

//  from src/corelib/mimetypes/qmimedatabase.cpp, line 268, as _ZNK20QMimeDatabasePrivate14fallbackParentERK7QString
inline QString QMimeDatabasePrivate::fallbackParent(const QString &mimeTypeName) const
{
    const QStringView myGroup = QStringView{mimeTypeName}.left(mimeTypeName.indexOf(u'/'));
    // All real-file mimetypes implicitly derive from application/octet-stream
    if (myGroup != "inode"_L1 &&
        // ignore non-file extensions
        myGroup != "all"_L1 && myGroup != "fonts"_L1 && myGroup != "print"_L1 && myGroup != "uri"_L1
        && mimeTypeName != defaultMimeType()) {
        return defaultMimeType();
    }
    return QString();
}
//  -----------------------------------------------------------------------

//  QMimeDatabasePrivate::QMimeDatabasePrivate()
extern "C" Q_DECL_EXPORT
QMimeDatabasePrivate *ritual_ZN20QMimeDatabasePrivateC1Ev() {
  return new QMimeDatabasePrivate();
}

//  QMimeDatabasePrivate::~QMimeDatabasePrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN20QMimeDatabasePrivateD1Ev(QMimeDatabasePrivate *self) {
  delete self;
}

//  const QString &QMimeDatabasePrivate::defaultMimeType() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QMimeDatabasePrivate15defaultMimeTypeEv(
    const QMimeDatabasePrivate *self) {
  return new QString(self->defaultMimeType());
}

//  bool QMimeDatabasePrivate::shouldCheck()
extern "C" Q_DECL_EXPORT
bool ritual_ZN20QMimeDatabasePrivate11shouldCheckEv(
    QMimeDatabasePrivate *self) {
  return self->shouldCheck();
}

//  QString QMimeDatabasePrivate::fallbackParent(const QString &mimeTypeName)
//      const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK20QMimeDatabasePrivate14fallbackParentERK7QString(
    const QMimeDatabasePrivate *self,
    const QString *mimeTypeName) {
  return new QString(self->fallbackParent(*mimeTypeName));
}

//  a QMimeTypePrivate::LocaleHash a ritual of QMimeDatabasePrivate gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMimeDatabasePrivate__QMimeTypePrivate_LocaleHash(
    QMimeTypePrivate::LocaleHash *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
