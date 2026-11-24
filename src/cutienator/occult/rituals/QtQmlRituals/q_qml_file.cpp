//  Written by dev_tooling.RitualGenerator from the records of
//  QtQml/qqmlfile.h, Qt 6.12.0. Changes made here are lost.
#include <QtQml/QtQml>
#include <QtQml/qqmlfile.h>
#include <QtCore/qurl.h>
#include <QtCore/qstring.h>
#include <QtCore/qbytearray.h>

#if QT_DEPRECATED_SINCE(6, 11)
//  QQmlFile::QQmlFile()
extern "C" Q_DECL_EXPORT
QQmlFile *ritual_ZN8QQmlFileC1Ev() {
  return new QQmlFile();
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  QQmlFile::QQmlFile(QQmlEngine *engine, const QUrl &url)
extern "C" Q_DECL_EXPORT
QQmlFile *ritual_ZN8QQmlFileC1EP10QQmlEngineRK4QUrl(
    QQmlEngine *engine,
    const QUrl *url) {
  return new QQmlFile(engine, *url);
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  QQmlFile::QQmlFile(QQmlEngine *engine, const QString &url)
extern "C" Q_DECL_EXPORT
QQmlFile *ritual_ZN8QQmlFileC1EP10QQmlEngineRK7QString(
    QQmlEngine *engine,
    const QString *url) {
  return new QQmlFile(engine, *url);
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  QQmlFile::~QQmlFile()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlFileD1Ev(QQmlFile *self) {
  delete self;
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  bool QQmlFile::isNull() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlFile6isNullEv(const QQmlFile *self) {
  return self->isNull();
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  bool QQmlFile::isReady() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlFile7isReadyEv(const QQmlFile *self) {
  return self->isReady();
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  bool QQmlFile::isError() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlFile7isErrorEv(const QQmlFile *self) {
  return self->isError();
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  bool QQmlFile::isLoading() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK8QQmlFile9isLoadingEv(const QQmlFile *self) {
  return self->isLoading();
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  QUrl QQmlFile::url() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK8QQmlFile3urlEv(const QQmlFile *self) {
  return new QUrl(self->url());
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  Status QQmlFile::status() const
extern "C" Q_DECL_EXPORT
QQmlFile::Status ritual_ZNK8QQmlFile6statusEv(const QQmlFile *self) {
  return self->status();
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  QString QQmlFile::error() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK8QQmlFile5errorEv(const QQmlFile *self) {
  return new QString(self->error());
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  qint64 QQmlFile::size() const
extern "C" Q_DECL_EXPORT
qint64 ritual_ZNK8QQmlFile4sizeEv(const QQmlFile *self) {
  return self->size();
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  const char *QQmlFile::data() const
extern "C" Q_DECL_EXPORT
const char *ritual_ZNK8QQmlFile4dataEv(const QQmlFile *self) {
  return self->data();
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  QByteArray QQmlFile::dataByteArray() const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK8QQmlFile13dataByteArrayEv(const QQmlFile *self) {
  return new QByteArray(self->dataByteArray());
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  void QQmlFile::load(QQmlEngine *a0, const QUrl &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlFile4loadEP10QQmlEngineRK4QUrl(
    QQmlFile *self,
    QQmlEngine *a0,
    const QUrl *a1) {
  self->load(a0, *a1);
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  void QQmlFile::load(QQmlEngine *a0, const QString &a1)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlFile4loadEP10QQmlEngineRK7QString(
    QQmlFile *self,
    QQmlEngine *a0,
    const QString *a1) {
  self->load(a0, *a1);
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  void QQmlFile::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlFile5clearEv(QQmlFile *self) {
  self->clear();
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
//  void QQmlFile::clear(QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN8QQmlFile5clearEP7QObject(QQmlFile *self, QObject *object) {
  self->clear(object);
}
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
#if QT_CONFIG(qml_network)
//  bool QQmlFile::connectFinished(QObject *a0, const char *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlFile15connectFinishedEP7QObjectPKc(
    QQmlFile *self,
    QObject *a0,
    const char *a1) {
  return self->connectFinished(a0, a1);
}
#endif  // QT_CONFIG(qml_network)
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
#if QT_CONFIG(qml_network)
//  bool QQmlFile::connectFinished(QObject *a0, int a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlFile15connectFinishedEP7QObjecti(
    QQmlFile *self,
    QObject *a0,
    int a1) {
  return self->connectFinished(a0, a1);
}
#endif  // QT_CONFIG(qml_network)
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
#if QT_CONFIG(qml_network)
//  bool QQmlFile::connectDownloadProgress(QObject *a0, const char *a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlFile23connectDownloadProgressEP7QObjectPKc(
    QQmlFile *self,
    QObject *a0,
    const char *a1) {
  return self->connectDownloadProgress(a0, a1);
}
#endif  // QT_CONFIG(qml_network)
#endif  // QT_DEPRECATED_SINCE(6, 11)

#if QT_DEPRECATED_SINCE(6, 11)
#if QT_CONFIG(qml_network)
//  bool QQmlFile::connectDownloadProgress(QObject *a0, int a1)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlFile23connectDownloadProgressEP7QObjecti(
    QQmlFile *self,
    QObject *a0,
    int a1) {
  return self->connectDownloadProgress(a0, a1);
}
#endif  // QT_CONFIG(qml_network)
#endif  // QT_DEPRECATED_SINCE(6, 11)

//  bool QQmlFile::isSynchronous(const QString &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlFile13isSynchronousERK7QString(const QString *url) {
  return QQmlFile::isSynchronous(*url);
}

//  bool QQmlFile::isSynchronous(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlFile13isSynchronousERK4QUrl(const QUrl *url) {
  return QQmlFile::isSynchronous(*url);
}

//  bool QQmlFile::isLocalFile(const QString &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlFile11isLocalFileERK7QString(const QString *url) {
  return QQmlFile::isLocalFile(*url);
}

//  bool QQmlFile::isLocalFile(const QUrl &url)
extern "C" Q_DECL_EXPORT
bool ritual_ZN8QQmlFile11isLocalFileERK4QUrl(const QUrl *url) {
  return QQmlFile::isLocalFile(*url);
}

//  QString QQmlFile::urlToLocalFileOrQrc(const QString &a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QQmlFile19urlToLocalFileOrQrcERK7QString(
    const QString *a0) {
  return new QString(QQmlFile::urlToLocalFileOrQrc(*a0));
}

//  QString QQmlFile::urlToLocalFileOrQrc(const QUrl &a0)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN8QQmlFile19urlToLocalFileOrQrcERK4QUrl(const QUrl *a0) {
  return new QString(QQmlFile::urlToLocalFileOrQrc(*a0));
}
