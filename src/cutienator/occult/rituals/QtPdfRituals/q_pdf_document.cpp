//  Written by dev_tooling.RitualGenerator from the records of
//  QtPdf/qpdfdocument.h, Qt 6.12.0. Changes made here are lost.
#include <QtPdf/qpdfdocument.h>
#include <QtCore/qstring.h>
#include <QtCore/qvariant.h>
#include <QtCore/qsize.h>
#include <QtPdf/qpdfdocumentrenderoptions.h>
#include <QtGui/qimage.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <QtPdf/qpdfselection.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QPdfDocument that Python can take functions over in. Every QPdfDocument
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPdfDocumentCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQPdfDocumentCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfDocumentCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfDocumentCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfDocumentCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfDocumentCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQPdfDocumentCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQPdfDocument : public QPdfDocument {
public:
  using QPdfDocument::QPdfDocument;
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
      CuteQPdfDocumentCall0 call = reinterpret_cast<CuteQPdfDocumentCall0>(taken[0]);
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
      CuteQPdfDocumentCall1 call = reinterpret_cast<CuteQPdfDocumentCall1>(taken[1]);
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
      CuteQPdfDocumentCall2 call = reinterpret_cast<CuteQPdfDocumentCall2>(taken[2]);
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
      CuteQPdfDocumentCall3 call = reinterpret_cast<CuteQPdfDocumentCall3>(taken[3]);
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
      CuteQPdfDocumentCall4 call = reinterpret_cast<CuteQPdfDocumentCall4>(taken[4]);
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
      CuteQPdfDocumentCall5 call = reinterpret_cast<CuteQPdfDocumentCall5>(taken[5]);
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
      CuteQPdfDocumentCall6 call = reinterpret_cast<CuteQPdfDocumentCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QPdfDocument::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QPdfDocument10metaObjectEv(
    const QPdfDocument *self) {
  return self->metaObject();
}

//  void *QPdfDocument::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QPdfDocument11qt_metacastEPKc(
    QPdfDocument *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QPdfDocument::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QPdfDocument11qt_metacallEN11QMetaObject4CallEiPPv(
    QPdfDocument *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QPdfDocument::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QPdfDocument2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QPdfDocument::tr(s, c, n));
}

//  QPdfDocument::QPdfDocument()
extern "C" Q_DECL_EXPORT
QPdfDocument *ritual_ZN12QPdfDocumentC1Ev() {
  return new CuteQPdfDocument();
}

//  QPdfDocument::QPdfDocument(QObject *parent)
extern "C" Q_DECL_EXPORT
QPdfDocument *ritual_ZN12QPdfDocumentC1EP7QObject(QObject *parent) {
  return new CuteQPdfDocument(parent);
}

//  QPdfDocument::~QPdfDocument()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPdfDocumentD1Ev(QPdfDocument *self) {
  delete self;
}

//  Error QPdfDocument::load(const QString &fileName)
extern "C" Q_DECL_EXPORT
QPdfDocument::Error ritual_ZN12QPdfDocument4loadERK7QString(
    QPdfDocument *self,
    const QString *fileName) {
  return self->load(*fileName);
}

//  Status QPdfDocument::status() const
extern "C" Q_DECL_EXPORT
QPdfDocument::Status ritual_ZNK12QPdfDocument6statusEv(
    const QPdfDocument *self) {
  return self->status();
}

//  void QPdfDocument::load(QIODevice *device)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPdfDocument4loadEP9QIODevice(
    QPdfDocument *self,
    QIODevice *device) {
  self->load(device);
}

//  void QPdfDocument::setPassword(const QString &password)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPdfDocument11setPasswordERK7QString(
    QPdfDocument *self,
    const QString *password) {
  self->setPassword(*password);
}

//  QString QPdfDocument::password() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPdfDocument8passwordEv(const QPdfDocument *self) {
  return new QString(self->password());
}

//  QVariant QPdfDocument::metaData(MetaDataField field) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK12QPdfDocument8metaDataENS_13MetaDataFieldE(
    const QPdfDocument *self,
    QPdfDocument::MetaDataField field) {
  return new QVariant(self->metaData(field));
}

//  Error QPdfDocument::error() const
extern "C" Q_DECL_EXPORT
QPdfDocument::Error ritual_ZNK12QPdfDocument5errorEv(
    const QPdfDocument *self) {
  return self->error();
}

//  void QPdfDocument::close()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPdfDocument5closeEv(QPdfDocument *self) {
  self->close();
}

//  int QPdfDocument::pageCount() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK12QPdfDocument9pageCountEv(const QPdfDocument *self) {
  return self->pageCount();
}

//  QSizeF QPdfDocument::pagePointSize(int page) const
extern "C" Q_DECL_EXPORT
QSizeF *ritual_ZNK12QPdfDocument13pagePointSizeEi(
    const QPdfDocument *self,
    int page) {
  return new QSizeF(self->pagePointSize(page));
}

//  QString QPdfDocument::pageLabel(int page)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QPdfDocument9pageLabelEi(QPdfDocument *self, int page) {
  return new QString(self->pageLabel(page));
}

//  int QPdfDocument::pageIndexForLabel(const QString &label)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QPdfDocument17pageIndexForLabelERK7QString(
    QPdfDocument *self,
    const QString *label) {
  return self->pageIndexForLabel(*label);
}

//  QAbstractListModel *QPdfDocument::pageModel()
extern "C" Q_DECL_EXPORT
QAbstractListModel *ritual_ZN12QPdfDocument9pageModelEv(QPdfDocument *self) {
  return self->pageModel();
}

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QImage QPdfDocument::render(int page, QSize imageSize,
//      QPdfDocumentRenderOptions options)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN12QPdfDocument6renderEi5QSize25QPdfDocumentRenderOptions(
    QPdfDocument *self,
    int page,
    const QSize *imageSize,
    const QPdfDocumentRenderOptions *options) {
  return new QImage(self->render(page, *imageSize, *options));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

#if QT_VERSION < QT_VERSION_CHECK(7, 0, 0)
//  QImage QPdfDocument::render(int page, QSize imageSize,
//      QPdfDocumentRenderOptions options, QImage::Format format, const
//      QColor &fillColor)
extern "C" Q_DECL_EXPORT
QImage *ritual_ZN12QPdfDocument6renderEi5QSize25QPdfDocumentRenderOptionsN6QImage6FormatERK6QColor(
    QPdfDocument *self,
    int page,
    const QSize *imageSize,
    const QPdfDocumentRenderOptions *options,
    QImage::Format format,
    const QColor *fillColor) {
  return new QImage(
      self->render(
          page,
          *imageSize,
          *options,
          format,
          *fillColor));
}
#endif  // QT_VERSION < QT_VERSION_CHECK(7, 0, 0)

//  QPdfSelection QPdfDocument::getSelection(int page, QPointF start, QPointF
//      end)
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN12QPdfDocument12getSelectionEi7QPointFS0_(
    QPdfDocument *self,
    int page,
    const QPointF *start,
    const QPointF *end) {
  return new QPdfSelection(self->getSelection(page, *start, *end));
}

//  QPdfSelection QPdfDocument::getSelectionAtIndex(int page, int startIndex,
//      int maxLength)
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN12QPdfDocument19getSelectionAtIndexEiii(
    QPdfDocument *self,
    int page,
    int startIndex,
    int maxLength) {
  return new QPdfSelection(
      self->getSelectionAtIndex(
          page,
          startIndex,
          maxLength));
}

//  QPdfSelection QPdfDocument::getAllText(int page)
extern "C" Q_DECL_EXPORT
QPdfSelection *ritual_ZN12QPdfDocument10getAllTextEi(
    QPdfDocument *self,
    int page) {
  return new QPdfSelection(self->getAllText(page));
}

//  void QPdfDocument::passwordChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPdfDocument15passwordChangedEv(QPdfDocument *self) {
  self->passwordChanged();
}

//  void QPdfDocument::passwordRequired()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPdfDocument16passwordRequiredEv(QPdfDocument *self) {
  self->passwordRequired();
}

//  void QPdfDocument::statusChanged(QPdfDocument::Status status)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPdfDocument13statusChangedENS_6StatusE(
    QPdfDocument *self,
    QPdfDocument::Status status) {
  self->statusChanged(status);
}

//  void QPdfDocument::pageCountChanged(int pageCount)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPdfDocument16pageCountChangedEi(
    QPdfDocument *self,
    int pageCount) {
  self->pageCountChanged(pageCount);
}

//  void QPdfDocument::pageModelChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QPdfDocument16pageModelChangedEv(QPdfDocument *self) {
  self->pageModelChanged();
}

//  QString QPdfDocument::fileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK12QPdfDocument8fileNameEv(const QPdfDocument *self) {
  return new QString(self->fileName());
}

//  a Python function taken by a CuteQPdfDocument, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QPdfDocument(
    QPdfDocument *self,
    const char *key,
    void *call) {
  return static_cast<CuteQPdfDocument *>(self)->take(key, call);
}
