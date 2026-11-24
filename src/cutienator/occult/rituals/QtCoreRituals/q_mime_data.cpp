//  Written by dev_tooling.RitualGenerator from the records of
//  QtCore/qmimedata.h, Qt 6.12.0. Changes made here are lost.
#include <QtCore/qmimedata.h>
#include <QtCore/qstring.h>
#include <QtCore/qurl.h>
#include <QtCore/qvariant.h>
#include <QtCore/qbytearray.h>
#include <QtCore/qmetatype.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QMimeData may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQMimeData : QMimeData {
  using QMimeData::retrieveData;
};

//  A QMimeData that Python can take functions over in. Every QMimeData
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQMimeDataCall0)(const void *, const QString *, int *);
typedef const QVariant * (*CuteQMimeDataCall1)(const void *, const QString *, const QMetaType *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMimeDataCall2)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQMimeDataCall3)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMimeDataCall4)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMimeDataCall5)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMimeDataCall6)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMimeDataCall7)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQMimeDataCall8)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQMimeData : public QMimeData {
public:
  using QMimeData::QMimeData;
  void *taken[9] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK9QMimeData9hasFormatERK7QString")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK9QMimeData12retrieveDataERK7QString9QMetaType")) {
      taken[1] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[2] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[3] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[4] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  bool QMimeData::hasFormat(const QString &mimetype) const
  bool hasFormat(const QString &mimetype) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQMimeDataCall0 call = reinterpret_cast<CuteQMimeDataCall0>(taken[0]);
      bool given = call(this, &mimetype, &handled);
      if (handled) return given;
    }
    return QMimeData::hasFormat(mimetype);
  }

  //  QVariant QMimeData::retrieveData(const QString &mimetype, QMetaType
  //      preferredType) const
  QVariant retrieveData(
      const QString &mimetype,
      QMetaType preferredType) const override {
    if (taken[1]) {
      int handled = 0;
      CuteQMimeDataCall1 call = reinterpret_cast<CuteQMimeDataCall1>(taken[1]);
      const QVariant * given = call(this, &mimetype, &preferredType, &handled);
      if (handled && given) return *given;
    }
    return QMimeData::retrieveData(mimetype, preferredType);
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQMimeDataCall2 call = reinterpret_cast<CuteQMimeDataCall2>(taken[2]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQMimeDataCall3 call = reinterpret_cast<CuteQMimeDataCall3>(taken[3]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQMimeDataCall4 call = reinterpret_cast<CuteQMimeDataCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQMimeDataCall5 call = reinterpret_cast<CuteQMimeDataCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQMimeDataCall6 call = reinterpret_cast<CuteQMimeDataCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[7]) {
      int handled = 0;
      CuteQMimeDataCall7 call = reinterpret_cast<CuteQMimeDataCall7>(taken[7]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[8]) {
      int handled = 0;
      CuteQMimeDataCall8 call = reinterpret_cast<CuteQMimeDataCall8>(taken[8]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QMimeData::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK9QMimeData10metaObjectEv(
    const QMimeData *self) {
  return self->metaObject();
}

//  QString QMimeData::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN9QMimeData2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QMimeData::tr(s, c, n));
}

//  QMimeData::QMimeData()
extern "C" Q_DECL_EXPORT
QMimeData *ritual_ZN9QMimeDataC1Ev() {
  return new CuteQMimeData();
}

//  QMimeData::~QMimeData()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeDataD1Ev(QMimeData *self) {
  delete self;
}

//  QList<QUrl> QMimeData::urls() const
extern "C" Q_DECL_EXPORT
QList<QUrl> *ritual_ZNK9QMimeData4urlsEv(const QMimeData *self) {
  return new QList<QUrl>(self->urls());
}

//  void QMimeData::setUrls(const QList<QUrl> &urls)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData7setUrlsERK5QListI4QUrlE(
    QMimeData *self,
    const QList<QUrl> *urls) {
  self->setUrls(*urls);
}

//  bool QMimeData::hasUrls() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData7hasUrlsEv(const QMimeData *self) {
  return self->hasUrls();
}

//  QString QMimeData::text() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeData4textEv(const QMimeData *self) {
  return new QString(self->text());
}

//  void QMimeData::setText(const QString &text)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData7setTextERK7QString(
    QMimeData *self,
    const QString *text) {
  self->setText(*text);
}

//  bool QMimeData::hasText() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData7hasTextEv(const QMimeData *self) {
  return self->hasText();
}

//  QString QMimeData::html() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK9QMimeData4htmlEv(const QMimeData *self) {
  return new QString(self->html());
}

//  void QMimeData::setHtml(const QString &html)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData7setHtmlERK7QString(
    QMimeData *self,
    const QString *html) {
  self->setHtml(*html);
}

//  bool QMimeData::hasHtml() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData7hasHtmlEv(const QMimeData *self) {
  return self->hasHtml();
}

//  QVariant QMimeData::imageData() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QMimeData9imageDataEv(const QMimeData *self) {
  return new QVariant(self->imageData());
}

//  void QMimeData::setImageData(const QVariant &image)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData12setImageDataERK8QVariant(
    QMimeData *self,
    const QVariant *image) {
  self->setImageData(*image);
}

//  bool QMimeData::hasImage() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData8hasImageEv(const QMimeData *self) {
  return self->hasImage();
}

//  QVariant QMimeData::colorData() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QMimeData9colorDataEv(const QMimeData *self) {
  return new QVariant(self->colorData());
}

//  void QMimeData::setColorData(const QVariant &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData12setColorDataERK8QVariant(
    QMimeData *self,
    const QVariant *color) {
  self->setColorData(*color);
}

//  bool QMimeData::hasColor() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData8hasColorEv(const QMimeData *self) {
  return self->hasColor();
}

//  QByteArray QMimeData::data(const QString &mimetype) const
extern "C" Q_DECL_EXPORT
QByteArray *ritual_ZNK9QMimeData4dataERK7QString(
    const QMimeData *self,
    const QString *mimetype) {
  return new QByteArray(self->data(*mimetype));
}

//  void QMimeData::setData(const QString &mimetype, const QByteArray &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData7setDataERK7QStringRK10QByteArray(
    QMimeData *self,
    const QString *mimetype,
    const QByteArray *data) {
  self->setData(*mimetype, *data);
}

//  void QMimeData::removeFormat(const QString &mimetype)
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData12removeFormatERK7QString(
    QMimeData *self,
    const QString *mimetype) {
  self->removeFormat(*mimetype);
}

//  bool QMimeData::hasFormat(const QString &mimetype) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK9QMimeData9hasFormatERK7QString(
    const QMimeData *self,
    const QString *mimetype) {
  return self->hasFormat(*mimetype);
}

//  QStringList QMimeData::formats() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK9QMimeData7formatsEv(const QMimeData *self) {
  return new QList<QString>(self->formats());
}

//  void QMimeData::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN9QMimeData5clearEv(QMimeData *self) {
  self->clear();
}

//  QVariant QMimeData::retrieveData(const QString &mimetype, QMetaType
//      preferredType) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK9QMimeData12retrieveDataERK7QString9QMetaType(
    const QMimeData *self,
    const QString *mimetype,
    const QMetaType *preferredType) {
  return new QVariant(self->retrieveData(*mimetype, *preferredType));
}

//  a Python function taken by a CuteQMimeData, for the function named by the
//      key
extern "C" Q_DECL_EXPORT
bool ritual_take_QMimeData(QMimeData *self, const char *key, void *call) {
  return static_cast<CuteQMimeData *>(self)->take(key, call);
}

//  bool QMimeData::hasFormat(const QString &mimetype) const
extern "C" Q_DECL_EXPORT
bool ritual_own_ZNK9QMimeData9hasFormatERK7QString(
    const QMimeData *self,
    const QString *mimetype) {
  return self->QMimeData::hasFormat(*mimetype);
}

//  QVariant QMimeData::retrieveData(const QString &mimetype, QMetaType
//      preferredType) const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK9QMimeData12retrieveDataERK7QString9QMetaType(
    const QMimeData *self,
    const QString *mimetype,
    const QMetaType *preferredType) {
  return new QVariant(
      static_cast<const OwnQMimeData *>(self)->OwnQMimeData::retrieveData(
          *mimetype,
          *preferredType));
}
