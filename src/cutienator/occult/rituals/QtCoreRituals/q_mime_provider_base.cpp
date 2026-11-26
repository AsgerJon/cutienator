//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/6.12.0/QtCore/private/qmimeprovider_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtCore/qglobal.h>
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#if QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCore/QtCore>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/6.12.0/QtCore/private/qmimeprovider_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QString>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/private/qmimeprovider_p.h>
#include <QtCore/private/qmimetypeparser_p.h>
#include <QtCore/qstandardpaths.h>
#include <QtCore/private/qmimemagicrulematcher_p.h>
#include <QtCore/QXmlStreamReader>
#include <QtCore/QBuffer>
#include <QtCore/QDir>
#include <QtCore/QFile>
#include <QtCore/QByteArrayMatcher>
#include <QtCore/QDebug>
#include <QtCore/QDateTime>
#include <QtCore/QtEndian>
#if QT_CONFIG(mimetype_database)
#  ifdef MIME_DATABASE_IS_ZSTD
#    include <zstd.h>
#  endif
#  ifdef MIME_DATABASE_IS_GZIP
#    include <zconf.h>
#    include <zlib.h>
#  endif
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 252, as _ZNK17QMimeProviderBase16overrideProviderEv
inline QMimeProviderBase *QMimeProviderBase::overrideProvider() const
{
    return m_overrideProvider;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 257, as _ZN17QMimeProviderBase19setOverrideProviderEPS_
inline void QMimeProviderBase::setOverrideProvider(QMimeProviderBase *provider)
{
    m_overrideProvider = provider;
}

//  from src/corelib/mimetypes/qmimeprovider.cpp, line 262, as _ZNK17QMimeProviderBase23isMimeTypeGlobsExcludedERK7QString
inline bool QMimeProviderBase::isMimeTypeGlobsExcluded(const QString &name) const
{
    if (m_overrideProvider) {
        if (m_overrideProvider->hasGlobDeleteAll(name))
            return true;
        return m_overrideProvider->isMimeTypeGlobsExcluded(name);
    }
    return false;
}
//  -----------------------------------------------------------------------

//  A QMimeProviderBase that Python can take functions over in. Every QMimeProviderBase
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(mimetype)
typedef bool (*CuteQMimeProviderBaseCall0)(const void *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef bool (*CuteQMimeProviderBaseCall1)(const void *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef bool (*CuteQMimeProviderBaseCall2)(const void *, const QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef QString * (*CuteQMimeProviderBaseCall3)(const void *, const QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef bool (*CuteQMimeProviderBaseCall4)(const void *, const QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef QString * (*CuteQMimeProviderBaseCall5)(const void *, const QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef QString * (*CuteQMimeProviderBaseCall6)(const void *, const QString *, int *);
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
typedef void (*CuteQMimeProviderBaseCall7)(const void *, int *);
#endif  // QT_CONFIG(mimetype)
class CuteQMimeProviderBase : public QMimeProviderBase {
public:
  using QMimeProviderBase::QMimeProviderBase;
  void *taken[8] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN17QMimeProviderBase7isValidEv")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZNK17QMimeProviderBase18isInternalDatabaseEv")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN17QMimeProviderBase13knowsMimeTypeERK7QString")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN17QMimeProviderBase12resolveAliasERK7QString")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN17QMimeProviderBase16hasGlobDeleteAllERK7QString")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN17QMimeProviderBase4iconERK7QString")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN17QMimeProviderBase11genericIconERK7QString")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
#if QT_CONFIG(mimetype)
    if (!std::strcmp(key, "_ZN17QMimeProviderBase12ensureLoadedEv")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(mimetype)
    return false;
  }

#if QT_CONFIG(mimetype)
  //  bool QMimeProviderBase::isValid()
  bool isValid() override {
    if (taken[0]) {
      int handled = 0;
      CuteQMimeProviderBaseCall0 call = reinterpret_cast<CuteQMimeProviderBaseCall0>(taken[0]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  bool QMimeProviderBase::isInternalDatabase() const
  bool isInternalDatabase() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMimeProviderBaseCall1 call = reinterpret_cast<CuteQMimeProviderBaseCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  bool QMimeProviderBase::knowsMimeType(const QString &name)
  bool knowsMimeType(const QString &name) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMimeProviderBaseCall2 call = reinterpret_cast<CuteQMimeProviderBaseCall2>(taken[2]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  QString QMimeProviderBase::resolveAlias(const QString &name)
  QString resolveAlias(const QString &name) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMimeProviderBaseCall3 call = reinterpret_cast<CuteQMimeProviderBaseCall3>(taken[3]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  bool QMimeProviderBase::hasGlobDeleteAll(const QString &name)
  bool hasGlobDeleteAll(const QString &name) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMimeProviderBaseCall4 call = reinterpret_cast<CuteQMimeProviderBaseCall4>(taken[4]);
      bool given = call(this, &name, &handled);
      if (handled) return given;
    }
    return {};
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  QString QMimeProviderBase::icon(const QString &name)
  QString icon(const QString &name) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMimeProviderBaseCall5 call = reinterpret_cast<CuteQMimeProviderBaseCall5>(taken[5]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  QString QMimeProviderBase::genericIcon(const QString &name)
  QString genericIcon(const QString &name) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMimeProviderBaseCall6 call = reinterpret_cast<CuteQMimeProviderBaseCall6>(taken[6]);
      QString * given = call(this, &name, &handled);
      if (handled && given) {
        QString back(*given);
        delete given;
        return back;
      }
    }
    return {};
  }
#endif  // QT_CONFIG(mimetype)

#if QT_CONFIG(mimetype)
  //  void QMimeProviderBase::ensureLoaded()
  void ensureLoaded() override {
    if (taken[7]) {
      int handled = 0;
      CuteQMimeProviderBaseCall7 call = reinterpret_cast<CuteQMimeProviderBaseCall7>(taken[7]);
      call(this, &handled);
      if (handled) return;
    }
    QMimeProviderBase::ensureLoaded();
  }
#endif  // QT_CONFIG(mimetype)
};

//  QMimeProviderBase::~QMimeProviderBase()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMimeProviderBaseD1Ev(QMimeProviderBase *self) {
  delete self;
}

//  bool QMimeProviderBase::isValid()
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QMimeProviderBase7isValidEv(QMimeProviderBase *self) {
  return self->isValid();
}

//  bool QMimeProviderBase::isInternalDatabase() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QMimeProviderBase18isInternalDatabaseEv(
    const QMimeProviderBase *self) {
  return self->isInternalDatabase();
}

//  bool QMimeProviderBase::knowsMimeType(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QMimeProviderBase13knowsMimeTypeERK7QString(
    QMimeProviderBase *self,
    const QString *name) {
  return self->knowsMimeType(*name);
}

//  void QMimeProviderBase::addFileNameMatches(const QString &fileName,
//      QMimeGlobMatchResult &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMimeProviderBase18addFileNameMatchesERK7QStringR20QMimeGlobMatchResult(
    QMimeProviderBase *self,
    const QString *fileName,
    QMimeGlobMatchResult *result) {
  self->addFileNameMatches(*fileName, *result);
}

//  void QMimeProviderBase::addParents(const QString &mime, QStringList
//      &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMimeProviderBase10addParentsERK7QStringR5QListIS0_E(
    QMimeProviderBase *self,
    const QString *mime,
    QStringList *result) {
  self->addParents(*mime, *result);
}

//  QString QMimeProviderBase::resolveAlias(const QString &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QMimeProviderBase12resolveAliasERK7QString(
    QMimeProviderBase *self,
    const QString *name) {
  return new QString(self->resolveAlias(*name));
}

//  void QMimeProviderBase::addAliases(const QString &name, QStringList
//      &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMimeProviderBase10addAliasesERK7QStringR5QListIS0_E(
    QMimeProviderBase *self,
    const QString *name,
    QStringList *result) {
  self->addAliases(*name, *result);
}

//  void QMimeProviderBase::findByMagic(const QByteArray &data,
//      QMimeMagicResult &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMimeProviderBase11findByMagicERK10QByteArrayR16QMimeMagicResult(
    QMimeProviderBase *self,
    const QByteArray *data,
    QMimeMagicResult *result) {
  self->findByMagic(*data, *result);
}

//  void QMimeProviderBase::addAllMimeTypes(QList<QMimeType> &result)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMimeProviderBase15addAllMimeTypesER5QListI9QMimeTypeE(
    QMimeProviderBase *self,
    QList<QMimeType> *result) {
  self->addAllMimeTypes(*result);
}

//  QMimeTypePrivate::LocaleHash QMimeProviderBase::localeComments(const
//      QString &name)
extern "C" Q_DECL_EXPORT
QMimeTypePrivate::LocaleHash *ritual_ZN17QMimeProviderBase14localeCommentsERK7QString(
    QMimeProviderBase *self,
    const QString *name) {
  return new QMimeTypePrivate::LocaleHash(self->localeComments(*name));
}

//  bool QMimeProviderBase::hasGlobDeleteAll(const QString &name)
extern "C" Q_DECL_EXPORT
bool ritual_ZN17QMimeProviderBase16hasGlobDeleteAllERK7QString(
    QMimeProviderBase *self,
    const QString *name) {
  return self->hasGlobDeleteAll(*name);
}

//  QStringList QMimeProviderBase::globPatterns(const QString &name)
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZN17QMimeProviderBase12globPatternsERK7QString(
    QMimeProviderBase *self,
    const QString *name) {
  return new QList<QString>(self->globPatterns(*name));
}

//  QString QMimeProviderBase::icon(const QString &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QMimeProviderBase4iconERK7QString(
    QMimeProviderBase *self,
    const QString *name) {
  return new QString(self->icon(*name));
}

//  QString QMimeProviderBase::genericIcon(const QString &name)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QMimeProviderBase11genericIconERK7QString(
    QMimeProviderBase *self,
    const QString *name) {
  return new QString(self->genericIcon(*name));
}

//  void QMimeProviderBase::ensureLoaded()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMimeProviderBase12ensureLoadedEv(QMimeProviderBase *self) {
  self->ensureLoaded();
}

//  QString QMimeProviderBase::directory() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QMimeProviderBase9directoryEv(
    const QMimeProviderBase *self) {
  return new QString(self->directory());
}

//  QMimeProviderBase *QMimeProviderBase::overrideProvider() const
extern "C" Q_DECL_EXPORT
QMimeProviderBase *ritual_ZNK17QMimeProviderBase16overrideProviderEv(
    const QMimeProviderBase *self) {
  return self->overrideProvider();
}

//  void QMimeProviderBase::setOverrideProvider(QMimeProviderBase *provider)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QMimeProviderBase19setOverrideProviderEPS_(
    QMimeProviderBase *self,
    QMimeProviderBase *provider) {
  self->setOverrideProvider(provider);
}

//  bool QMimeProviderBase::isMimeTypeGlobsExcluded(const QString &name)
//      const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QMimeProviderBase23isMimeTypeGlobsExcludedERK7QString(
    const QMimeProviderBase *self,
    const QString *name) {
  return self->isMimeTypeGlobsExcluded(*name);
}

//  a Python function taken by a CuteQMimeProviderBase, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMimeProviderBase(
    QMimeProviderBase *self,
    const char *key,
    void *call) {
  return static_cast<CuteQMimeProviderBase *>(self)->take(key, call);
}

//  void QMimeProviderBase::ensureLoaded()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN17QMimeProviderBase12ensureLoadedEv(
    QMimeProviderBase *self) {
  self->QMimeProviderBase::ensureLoaded();
}

//  a QMimeTypePrivate::LocaleHash a ritual of QMimeProviderBase gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QMimeProviderBase__QMimeTypePrivate_LocaleHash(
    QMimeTypePrivate::LocaleHash *self) {
  delete self;
}

#endif  // QT_CONFIG(mimetype)
#endif  // QT_CONFIG(mimetype)
