//  Written by dev_tooling.RitualGenerator from the records of
//  QtHelp/qhelpenginecore.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qglobal.h>
#include <QtHelp/qhelpenginecore.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qbytearray.h>
#include <QtHelp/qhelplink.h>
#include <QtCore/qvariant.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>
#include <QtCore/QList>
#include <QtCore/QStringList>
#include <QtCore/QString>
#include <QtCore/QFuture>
#include <memory>
#include <QtHelp/QHelpContentItem>

//  A QHelpEngineCore that Python can take functions over in. Every QHelpEngineCore
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpEngineCoreCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQHelpEngineCoreCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCoreCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCoreCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCoreCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCoreCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQHelpEngineCoreCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQHelpEngineCore : public QHelpEngineCore {
public:
  using QHelpEngineCore::QHelpEngineCore;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQHelpEngineCoreCall0 call = reinterpret_cast<CuteQHelpEngineCoreCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQHelpEngineCoreCall1 call = reinterpret_cast<CuteQHelpEngineCoreCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQHelpEngineCoreCall2 call = reinterpret_cast<CuteQHelpEngineCoreCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQHelpEngineCoreCall3 call = reinterpret_cast<CuteQHelpEngineCoreCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQHelpEngineCoreCall4 call = reinterpret_cast<CuteQHelpEngineCoreCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQHelpEngineCoreCall5 call = reinterpret_cast<CuteQHelpEngineCoreCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQHelpEngineCoreCall6 call = reinterpret_cast<CuteQHelpEngineCoreCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QHelpEngineCore::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK15QHelpEngineCore10metaObjectEv(
    const QHelpEngineCore *self) {
  return self->metaObject();
}

//  void *QHelpEngineCore::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN15QHelpEngineCore11qt_metacastEPKc(
    QHelpEngineCore *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QHelpEngineCore::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN15QHelpEngineCore11qt_metacallEN11QMetaObject4CallEiPPv(
    QHelpEngineCore *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QHelpEngineCore::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QHelpEngineCore2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QHelpEngineCore::tr(s, c, n));
}

//  QHelpEngineCore::QHelpEngineCore(const QString &collectionFile, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QHelpEngineCore *ritual_ZN15QHelpEngineCoreC1ERK7QStringP7QObject(
    const QString *collectionFile,
    QObject *parent) {
  return new CuteQHelpEngineCore(*collectionFile, parent);
}

//  QHelpEngineCore::~QHelpEngineCore()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCoreD1Ev(QHelpEngineCore *self) {
  delete self;
}

//  bool QHelpEngineCore::isReadOnly() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QHelpEngineCore10isReadOnlyEv(const QHelpEngineCore *self) {
  return self->isReadOnly();
}

//  void QHelpEngineCore::setReadOnly(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore11setReadOnlyEb(
    QHelpEngineCore *self,
    bool enable) {
  self->setReadOnly(enable);
}

//  QHelpFilterEngine *QHelpEngineCore::filterEngine() const
extern "C" Q_DECL_EXPORT
QHelpFilterEngine *ritual_ZNK15QHelpEngineCore12filterEngineEv(
    const QHelpEngineCore *self) {
  return self->filterEngine();
}

//  bool QHelpEngineCore::setupData()
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHelpEngineCore9setupDataEv(QHelpEngineCore *self) {
  return self->setupData();
}

//  QString QHelpEngineCore::collectionFile() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QHelpEngineCore14collectionFileEv(
    const QHelpEngineCore *self) {
  return new QString(self->collectionFile());
}

//  void QHelpEngineCore::setCollectionFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore17setCollectionFileERK7QString(
    QHelpEngineCore *self,
    const QString *fileName) {
  self->setCollectionFile(*fileName);
}

//  bool QHelpEngineCore::copyCollectionFile(const QString &fileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHelpEngineCore18copyCollectionFileERK7QString(
    QHelpEngineCore *self,
    const QString *fileName) {
  return self->copyCollectionFile(*fileName);
}

//  QString QHelpEngineCore::namespaceName(const QString
//      &documentationFileName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QHelpEngineCore13namespaceNameERK7QString(
    const QString *documentationFileName) {
  return new QString(QHelpEngineCore::namespaceName(*documentationFileName));
}

//  bool QHelpEngineCore::registerDocumentation(const QString
//      &documentationFileName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHelpEngineCore21registerDocumentationERK7QString(
    QHelpEngineCore *self,
    const QString *documentationFileName) {
  return self->registerDocumentation(*documentationFileName);
}

//  bool QHelpEngineCore::unregisterDocumentation(const QString
//      &namespaceName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHelpEngineCore23unregisterDocumentationERK7QString(
    QHelpEngineCore *self,
    const QString *namespaceName) {
  return self->unregisterDocumentation(*namespaceName);
}

//  QString QHelpEngineCore::documentationFileName(const QString
//      &namespaceName)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN15QHelpEngineCore21documentationFileNameERK7QString(
    QHelpEngineCore *self,
    const QString *namespaceName) {
  return new QString(self->documentationFileName(*namespaceName));
}

//  QStringList QHelpEngineCore::registeredDocumentations() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QHelpEngineCore24registeredDocumentationsEv(
    const QHelpEngineCore *self) {
  return new QList<QString>(self->registeredDocumentations());
}

//  QByteArray QHelpEngineCore::fileData(const QUrl &url) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK15QHelpEngineCore8fileDataERK4QUrl(
    const QHelpEngineCore *self,
    const QUrl *url) {
  return new QByteArray(self->fileData(*url));
}

//  QStringList QHelpEngineCore::customFilters() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QHelpEngineCore13customFiltersEv(
    const QHelpEngineCore *self) {
  return new QList<QString>(self->customFilters());
}

//  bool QHelpEngineCore::removeCustomFilter(const QString &filterName)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHelpEngineCore18removeCustomFilterERK7QString(
    QHelpEngineCore *self,
    const QString *filterName) {
  return self->removeCustomFilter(*filterName);
}

//  bool QHelpEngineCore::addCustomFilter(const QString &filterName, const
//      QStringList &attributes)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHelpEngineCore15addCustomFilterERK7QStringRK5QListIS0_E(
    QHelpEngineCore *self,
    const QString *filterName,
    const QList<QString> *attributes) {
  return self->addCustomFilter(*filterName, *attributes);
}

//  QStringList QHelpEngineCore::filterAttributes() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QHelpEngineCore16filterAttributesEv(
    const QHelpEngineCore *self) {
  return new QList<QString>(self->filterAttributes());
}

//  QStringList QHelpEngineCore::filterAttributes(const QString &filterName)
//      const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK15QHelpEngineCore16filterAttributesERK7QString(
    const QHelpEngineCore *self,
    const QString *filterName) {
  return new QList<QString>(self->filterAttributes(*filterName));
}

//  QString QHelpEngineCore::currentFilter() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QHelpEngineCore13currentFilterEv(
    const QHelpEngineCore *self) {
  return new QString(self->currentFilter());
}

//  void QHelpEngineCore::setCurrentFilter(const QString &filterName)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore16setCurrentFilterERK7QString(
    QHelpEngineCore *self,
    const QString *filterName) {
  self->setCurrentFilter(*filterName);
}

//  QList<QStringList> QHelpEngineCore::filterAttributeSets(const QString
//      &namespaceName) const
extern "C" Q_DECL_EXPORT
QList<QStringList> *ritual_ZNK15QHelpEngineCore19filterAttributeSetsERK7QString(
    const QHelpEngineCore *self,
    const QString *namespaceName) {
  return new QList<QStringList>(self->filterAttributeSets(*namespaceName));
}

//  QList<QUrl> QHelpEngineCore::files(const QString namespaceName, const
//      QStringList &filterAttributes, const QString &extensionFilter)
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZN15QHelpEngineCore5filesE7QStringRK5QListIS0_ERKS0_(
    QHelpEngineCore *self,
    const QString *namespaceName,
    const QList<QString> *filterAttributes,
    const QString *extensionFilter) {
  return new QList<QUrl>(
      self->files(
          *namespaceName,
          *filterAttributes,
          *extensionFilter));
}

//  QList<QUrl> QHelpEngineCore::files(const QString namespaceName, const
//      QString &filterName, const QString &extensionFilter)
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZN15QHelpEngineCore5filesE7QStringRKS0_S2_(
    QHelpEngineCore *self,
    const QString *namespaceName,
    const QString *filterName,
    const QString *extensionFilter) {
  return new QList<QUrl>(
      self->files(
          *namespaceName,
          *filterName,
          *extensionFilter));
}

//  QUrl QHelpEngineCore::findFile(const QUrl &url) const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK15QHelpEngineCore8findFileERK4QUrl(
    const QHelpEngineCore *self,
    const QUrl *url) {
  return new QUrl(self->findFile(*url));
}

//  QList<QHelpLink> QHelpEngineCore::documentsForIdentifier(const QString
//      &id) const
extern "C" Q_DECL_EXPORT
QList<QHelpLink> *ritual_ZNK15QHelpEngineCore22documentsForIdentifierERK7QString(
    const QHelpEngineCore *self,
    const QString *id) {
  return new QList<QHelpLink>(self->documentsForIdentifier(*id));
}

//  QList<QHelpLink> QHelpEngineCore::documentsForIdentifier(const QString
//      &id, const QString &filterName) const
extern "C" Q_DECL_EXPORT
QList<QHelpLink> *ritual_ZNK15QHelpEngineCore22documentsForIdentifierERK7QStringS2_(
    const QHelpEngineCore *self,
    const QString *id,
    const QString *filterName) {
  return new QList<QHelpLink>(
      self->documentsForIdentifier(
          *id,
          *filterName));
}

//  QList<QHelpLink> QHelpEngineCore::documentsForKeyword(const QString
//      &keyword) const
extern "C" Q_DECL_EXPORT
QList<QHelpLink> *ritual_ZNK15QHelpEngineCore19documentsForKeywordERK7QString(
    const QHelpEngineCore *self,
    const QString *keyword) {
  return new QList<QHelpLink>(self->documentsForKeyword(*keyword));
}

//  QList<QHelpLink> QHelpEngineCore::documentsForKeyword(const QString
//      &keyword, const QString &filterName) const
extern "C" Q_DECL_EXPORT
QList<QHelpLink> *ritual_ZNK15QHelpEngineCore19documentsForKeywordERK7QStringS2_(
    const QHelpEngineCore *self,
    const QString *keyword,
    const QString *filterName) {
  return new QList<QHelpLink>(
      self->documentsForKeyword(
          *keyword,
          *filterName));
}

//  bool QHelpEngineCore::removeCustomValue(const QString &key)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHelpEngineCore17removeCustomValueERK7QString(
    QHelpEngineCore *self,
    const QString *key) {
  return self->removeCustomValue(*key);
}

//  QVariant QHelpEngineCore::customValue(const QString &key, const QVariant
//      &defaultValue) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK15QHelpEngineCore11customValueERK7QStringRK8QVariant(
    const QHelpEngineCore *self,
    const QString *key,
    const QVariant *defaultValue) {
  return new QVariant(self->customValue(*key, *defaultValue));
}

//  bool QHelpEngineCore::setCustomValue(const QString &key, const QVariant
//      &value)
extern "C" Q_DECL_EXPORT
bool ritual_ZN15QHelpEngineCore14setCustomValueERK7QStringRK8QVariant(
    QHelpEngineCore *self,
    const QString *key,
    const QVariant *value) {
  return self->setCustomValue(*key, *value);
}

//  QVariant QHelpEngineCore::metaData(const QString &documentationFileName,
//      const QString &name)
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZN15QHelpEngineCore8metaDataERK7QStringS2_(
    const QString *documentationFileName,
    const QString *name) {
  return new QVariant(
      QHelpEngineCore::metaData(
          *documentationFileName,
          *name));
}

//  QString QHelpEngineCore::error() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK15QHelpEngineCore5errorEv(const QHelpEngineCore *self) {
  return new QString(self->error());
}

//  void QHelpEngineCore::setAutoSaveFilter(bool save)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore17setAutoSaveFilterEb(
    QHelpEngineCore *self,
    bool save) {
  self->setAutoSaveFilter(save);
}

//  bool QHelpEngineCore::autoSaveFilter() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QHelpEngineCore14autoSaveFilterEv(
    const QHelpEngineCore *self) {
  return self->autoSaveFilter();
}

//  void QHelpEngineCore::setUsesFilterEngine(bool uses)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore19setUsesFilterEngineEb(
    QHelpEngineCore *self,
    bool uses) {
  self->setUsesFilterEngine(uses);
}

//  bool QHelpEngineCore::usesFilterEngine() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK15QHelpEngineCore16usesFilterEngineEv(
    const QHelpEngineCore *self) {
  return self->usesFilterEngine();
}

#if QT_CONFIG(future)
//  QFuture<std::shared_ptr<QHelpContentItem>>
//      QHelpEngineCore::requestContentForCurrentFilter() const
extern "C" Q_DECL_EXPORT
QFuture<std::shared_ptr<QHelpContentItem>> *ritual_ZNK15QHelpEngineCore30requestContentForCurrentFilterEv(
    const QHelpEngineCore *self) {
  return new QFuture<std::shared_ptr<QHelpContentItem>>(
      self->requestContentForCurrentFilter());
}
#endif  // QT_CONFIG(future)

#if QT_CONFIG(future)
//  QFuture<std::shared_ptr<QHelpContentItem>>
//      QHelpEngineCore::requestContent(const QString &filter) const
extern "C" Q_DECL_EXPORT
QFuture<std::shared_ptr<QHelpContentItem>> *ritual_ZNK15QHelpEngineCore14requestContentERK7QString(
    const QHelpEngineCore *self,
    const QString *filter) {
  return new QFuture<std::shared_ptr<QHelpContentItem>>(
      self->requestContent(
          *filter));
}
#endif  // QT_CONFIG(future)

#if QT_CONFIG(future)
//  QFuture<QStringList> QHelpEngineCore::requestIndexForCurrentFilter()
//      const
extern "C" Q_DECL_EXPORT
QFuture<QStringList> *ritual_ZNK15QHelpEngineCore28requestIndexForCurrentFilterEv(
    const QHelpEngineCore *self) {
  return new QFuture<QStringList>(self->requestIndexForCurrentFilter());
}
#endif  // QT_CONFIG(future)

#if QT_CONFIG(future)
//  QFuture<QStringList> QHelpEngineCore::requestIndex(const QString &filter)
//      const
extern "C" Q_DECL_EXPORT
QFuture<QStringList> *ritual_ZNK15QHelpEngineCore12requestIndexERK7QString(
    const QHelpEngineCore *self,
    const QString *filter) {
  return new QFuture<QStringList>(self->requestIndex(*filter));
}
#endif  // QT_CONFIG(future)

//  void QHelpEngineCore::setupStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore12setupStartedEv(QHelpEngineCore *self) {
  self->setupStarted();
}

//  void QHelpEngineCore::setupFinished()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore13setupFinishedEv(QHelpEngineCore *self) {
  self->setupFinished();
}

//  void QHelpEngineCore::warning(const QString &msg)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore7warningERK7QString(
    QHelpEngineCore *self,
    const QString *msg) {
  self->warning(*msg);
}

//  void QHelpEngineCore::currentFilterChanged(const QString &newFilter)
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore20currentFilterChangedERK7QString(
    QHelpEngineCore *self,
    const QString *newFilter) {
  self->currentFilterChanged(*newFilter);
}

//  void QHelpEngineCore::readersAboutToBeInvalidated()
extern "C" Q_DECL_EXPORT
void ritual_ZN15QHelpEngineCore27readersAboutToBeInvalidatedEv(
    QHelpEngineCore *self) {
  self->readersAboutToBeInvalidated();
}

#if QT_DEPRECATED_SINCE(6, 8)
//  QHelpEngineCore::QHelpEngineCore(QHelpEngineCorePrivate
//      *helpEngineCorePrivate, QObject *parent)
extern "C" Q_DECL_EXPORT
QHelpEngineCore *ritual_ZN15QHelpEngineCoreC1EP22QHelpEngineCorePrivateP7QObject(
    QHelpEngineCorePrivate *helpEngineCorePrivate,
    QObject *parent) {
  return new CuteQHelpEngineCore(helpEngineCorePrivate, parent);
}
#endif  // QT_DEPRECATED_SINCE(6, 8)

//  a Python function taken by a CuteQHelpEngineCore, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QHelpEngineCore(
    QHelpEngineCore *self,
    const char *key,
    void *call) {
  return static_cast<CuteQHelpEngineCore *>(self)->take(key, call);
}

//  a QList<QStringList> a ritual of QHelpEngineCore gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpEngineCore__QList_QStringList(
    QList<QStringList> *self) {
  delete self;
}

//  a QFuture<std::shared_ptr<QHelpContentItem>> a ritual of QHelpEngineCore
//      gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpEngineCore__QFuture_std_shared_ptr_QHelpContentItem(
    QFuture<std::shared_ptr<QHelpContentItem>> *self) {
  delete self;
}

//  a QFuture<QStringList> a ritual of QHelpEngineCore gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QHelpEngineCore__QFuture_QStringList(
    QFuture<QStringList> *self) {
  delete self;
}
