//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebengineextensioninfo.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWebEngineCore/qtwebenginecoreglobal.h>
#if QT_CONFIG(webengine_extensions)
#include <QtWebEngineCore/qwebengineextensioninfo.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qlist.h>

//  QWebEngineExtensionInfo::QWebEngineExtensionInfo()
extern "C" Q_DECL_EXPORT
QWebEngineExtensionInfo *ritual_ZN23QWebEngineExtensionInfoC1Ev() {
  return new QWebEngineExtensionInfo();
}

//  QWebEngineExtensionInfo::QWebEngineExtensionInfo(const
//      QWebEngineExtensionInfo &other)
extern "C" Q_DECL_EXPORT
QWebEngineExtensionInfo *ritual_ZN23QWebEngineExtensionInfoC1ERKS_(
    const QWebEngineExtensionInfo *other) {
  return new QWebEngineExtensionInfo(*other);
}

//  QWebEngineExtensionInfo::QWebEngineExtensionInfo(QWebEngineExtensionInfo
//      &&other)
extern "C" Q_DECL_EXPORT
QWebEngineExtensionInfo *ritual_ZN23QWebEngineExtensionInfoC1EOS_(
    QWebEngineExtensionInfo *other) {
  return new QWebEngineExtensionInfo(std::move(*other));
}

//  QWebEngineExtensionInfo &QWebEngineExtensionInfo::operator=(const
//      QWebEngineExtensionInfo &other)
extern "C" Q_DECL_EXPORT
QWebEngineExtensionInfo *ritual_ZN23QWebEngineExtensionInfoaSERKS_(
    QWebEngineExtensionInfo *self,
    const QWebEngineExtensionInfo *other) {
  return &(self->operator=(*other));
}

//  QWebEngineExtensionInfo::~QWebEngineExtensionInfo()
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebEngineExtensionInfoD1Ev(QWebEngineExtensionInfo *self) {
  delete self;
}

//  QWebEngineExtensionInfo
//      &QWebEngineExtensionInfo::operator=(QWebEngineExtensionInfo &&other)
extern "C" Q_DECL_EXPORT
QWebEngineExtensionInfo *ritual_ZN23QWebEngineExtensionInfoaSEOS_(
    QWebEngineExtensionInfo *self,
    QWebEngineExtensionInfo *other) {
  return &(self->operator=(std::move(*other)));
}

//  void QWebEngineExtensionInfo::swap(QWebEngineExtensionInfo &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN23QWebEngineExtensionInfo4swapERS_(
    QWebEngineExtensionInfo *self,
    QWebEngineExtensionInfo *other) {
  self->swap(*other);
}

//  QString QWebEngineExtensionInfo::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QWebEngineExtensionInfo4nameEv(
    const QWebEngineExtensionInfo *self) {
  return new QString(self->name());
}

//  QString QWebEngineExtensionInfo::id() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QWebEngineExtensionInfo2idEv(
    const QWebEngineExtensionInfo *self) {
  return new QString(self->id());
}

//  QString QWebEngineExtensionInfo::description() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QWebEngineExtensionInfo11descriptionEv(
    const QWebEngineExtensionInfo *self) {
  return new QString(self->description());
}

//  QString QWebEngineExtensionInfo::path() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QWebEngineExtensionInfo4pathEv(
    const QWebEngineExtensionInfo *self) {
  return new QString(self->path());
}

//  QString QWebEngineExtensionInfo::error() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK23QWebEngineExtensionInfo5errorEv(
    const QWebEngineExtensionInfo *self) {
  return new QString(self->error());
}

//  QUrl QWebEngineExtensionInfo::actionPopupUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK23QWebEngineExtensionInfo14actionPopupUrlEv(
    const QWebEngineExtensionInfo *self) {
  return new QUrl(self->actionPopupUrl());
}

//  bool QWebEngineExtensionInfo::isEnabled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QWebEngineExtensionInfo9isEnabledEv(
    const QWebEngineExtensionInfo *self) {
  return self->isEnabled();
}

//  bool QWebEngineExtensionInfo::isLoaded() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QWebEngineExtensionInfo8isLoadedEv(
    const QWebEngineExtensionInfo *self) {
  return self->isLoaded();
}

//  bool QWebEngineExtensionInfo::isInstalled() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK23QWebEngineExtensionInfo11isInstalledEv(
    const QWebEngineExtensionInfo *self) {
  return self->isInstalled();
}

//  QWebEngineExtensionInfo::QWebEngineExtensionInfo(QWebEngineExtensionInfoP
//      rivate *d)
extern "C" Q_DECL_EXPORT
QWebEngineExtensionInfo *ritual_ZN23QWebEngineExtensionInfoC1EP30QWebEngineExtensionInfoPrivate(
    QWebEngineExtensionInfoPrivate *d) {
  return new QWebEngineExtensionInfo(d);
}

//  QList<QWebEngineExtensionInfo>::QList()
extern "C" Q_DECL_EXPORT
QList<QWebEngineExtensionInfo> *ritual_list_make_QWebEngineExtensionInfo() {
  return new QList<QWebEngineExtensionInfo>();
}

//  void QList<QWebEngineExtensionInfo>::append(const QWebEngineExtensionInfo
//      &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWebEngineExtensionInfo(
    QList<QWebEngineExtensionInfo> *self,
    const QWebEngineExtensionInfo *element) {
  self->append(*element);
}

//  qsizetype QList<QWebEngineExtensionInfo>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWebEngineExtensionInfo(
    const QList<QWebEngineExtensionInfo> *self) {
  return self->size();
}

//  const QWebEngineExtensionInfo
//      &QList<QWebEngineExtensionInfo>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWebEngineExtensionInfo *ritual_list_at_QWebEngineExtensionInfo(
    const QList<QWebEngineExtensionInfo> *self,
    long long index) {
  return new QWebEngineExtensionInfo(self->at(index));
}

//  QList<QWebEngineExtensionInfo>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWebEngineExtensionInfo(
    QList<QWebEngineExtensionInfo> *self) {
  delete self;
}

#endif  // QT_CONFIG(webengine_extensions)
