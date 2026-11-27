//  Written by dev_tooling.RitualGenerator from the records of
//  QtWebEngineCore/qwebenginecontextmenurequest.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtWebEngineCore/qwebenginecontextmenurequest.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtCore/qurl.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWebEngineContextMenuRequest that Python can take functions over in. Every QWebEngineContextMenuRequest
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineContextMenuRequestCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWebEngineContextMenuRequestCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineContextMenuRequestCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineContextMenuRequestCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineContextMenuRequestCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineContextMenuRequestCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWebEngineContextMenuRequestCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWebEngineContextMenuRequest : public QWebEngineContextMenuRequest {
public:
  using QWebEngineContextMenuRequest::QWebEngineContextMenuRequest;
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
      CuteQWebEngineContextMenuRequestCall0 call = reinterpret_cast<CuteQWebEngineContextMenuRequestCall0>(taken[0]);
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
      CuteQWebEngineContextMenuRequestCall1 call = reinterpret_cast<CuteQWebEngineContextMenuRequestCall1>(taken[1]);
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
      CuteQWebEngineContextMenuRequestCall2 call = reinterpret_cast<CuteQWebEngineContextMenuRequestCall2>(taken[2]);
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
      CuteQWebEngineContextMenuRequestCall3 call = reinterpret_cast<CuteQWebEngineContextMenuRequestCall3>(taken[3]);
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
      CuteQWebEngineContextMenuRequestCall4 call = reinterpret_cast<CuteQWebEngineContextMenuRequestCall4>(taken[4]);
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
      CuteQWebEngineContextMenuRequestCall5 call = reinterpret_cast<CuteQWebEngineContextMenuRequestCall5>(taken[5]);
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
      CuteQWebEngineContextMenuRequestCall6 call = reinterpret_cast<CuteQWebEngineContextMenuRequestCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWebEngineContextMenuRequest::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK28QWebEngineContextMenuRequest10metaObjectEv(
    const QWebEngineContextMenuRequest *self) {
  return self->metaObject();
}

//  void *QWebEngineContextMenuRequest::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN28QWebEngineContextMenuRequest11qt_metacastEPKc(
    QWebEngineContextMenuRequest *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWebEngineContextMenuRequest::qt_metacall(QMetaObject::Call a0, int
//      a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN28QWebEngineContextMenuRequest11qt_metacallEN11QMetaObject4CallEiPPv(
    QWebEngineContextMenuRequest *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWebEngineContextMenuRequest::tr(const char *s, const char *c,
//      int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN28QWebEngineContextMenuRequest2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWebEngineContextMenuRequest::tr(s, c, n));
}

//  QWebEngineContextMenuRequest::~QWebEngineContextMenuRequest()
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineContextMenuRequestD1Ev(
    QWebEngineContextMenuRequest *self) {
  delete self;
}

//  QPoint QWebEngineContextMenuRequest::position() const
extern "C" Q_DECL_EXPORT
QPoint *ritual_ZNK28QWebEngineContextMenuRequest8positionEv(
    const QWebEngineContextMenuRequest *self) {
  return new QPoint(self->position());
}

//  QString QWebEngineContextMenuRequest::selectedText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QWebEngineContextMenuRequest12selectedTextEv(
    const QWebEngineContextMenuRequest *self) {
  return new QString(self->selectedText());
}

//  QString QWebEngineContextMenuRequest::linkText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QWebEngineContextMenuRequest8linkTextEv(
    const QWebEngineContextMenuRequest *self) {
  return new QString(self->linkText());
}

//  QUrl QWebEngineContextMenuRequest::linkUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK28QWebEngineContextMenuRequest7linkUrlEv(
    const QWebEngineContextMenuRequest *self) {
  return new QUrl(self->linkUrl());
}

//  QUrl QWebEngineContextMenuRequest::mediaUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK28QWebEngineContextMenuRequest8mediaUrlEv(
    const QWebEngineContextMenuRequest *self) {
  return new QUrl(self->mediaUrl());
}

//  MediaType QWebEngineContextMenuRequest::mediaType() const
extern "C" Q_DECL_EXPORT
QWebEngineContextMenuRequest::MediaType ritual_ZNK28QWebEngineContextMenuRequest9mediaTypeEv(
    const QWebEngineContextMenuRequest *self) {
  return self->mediaType();
}

//  bool QWebEngineContextMenuRequest::isContentEditable() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QWebEngineContextMenuRequest17isContentEditableEv(
    const QWebEngineContextMenuRequest *self) {
  return self->isContentEditable();
}

//  QString QWebEngineContextMenuRequest::misspelledWord() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QWebEngineContextMenuRequest14misspelledWordEv(
    const QWebEngineContextMenuRequest *self) {
  return new QString(self->misspelledWord());
}

//  QStringList QWebEngineContextMenuRequest::spellCheckerSuggestions() const
extern "C" Q_DECL_EXPORT
QList<QString> *ritual_ZNK28QWebEngineContextMenuRequest23spellCheckerSuggestionsEv(
    const QWebEngineContextMenuRequest *self) {
  return new QList<QString>(self->spellCheckerSuggestions());
}

//  bool QWebEngineContextMenuRequest::isAccepted() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QWebEngineContextMenuRequest10isAcceptedEv(
    const QWebEngineContextMenuRequest *self) {
  return self->isAccepted();
}

//  void QWebEngineContextMenuRequest::setAccepted(bool accepted)
extern "C" Q_DECL_EXPORT
void ritual_ZN28QWebEngineContextMenuRequest11setAcceptedEb(
    QWebEngineContextMenuRequest *self,
    bool accepted) {
  self->setAccepted(accepted);
}

//  MediaFlags QWebEngineContextMenuRequest::mediaFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QWebEngineContextMenuRequest10mediaFlagsEv(
    const QWebEngineContextMenuRequest *self) {
  return static_cast<int>(self->mediaFlags().toInt());
}

//  EditFlags QWebEngineContextMenuRequest::editFlags() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK28QWebEngineContextMenuRequest9editFlagsEv(
    const QWebEngineContextMenuRequest *self) {
  return static_cast<int>(self->editFlags().toInt());
}

//  QUrl QWebEngineContextMenuRequest::filteredLinkUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK28QWebEngineContextMenuRequest15filteredLinkUrlEv(
    const QWebEngineContextMenuRequest *self) {
  return new QUrl(self->filteredLinkUrl());
}

//  QString QWebEngineContextMenuRequest::altText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QWebEngineContextMenuRequest7altTextEv(
    const QWebEngineContextMenuRequest *self) {
  return new QString(self->altText());
}

//  QString QWebEngineContextMenuRequest::titleText() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QWebEngineContextMenuRequest9titleTextEv(
    const QWebEngineContextMenuRequest *self) {
  return new QString(self->titleText());
}

//  QUrl QWebEngineContextMenuRequest::referrerUrl() const
extern "C" Q_DECL_EXPORT
QUrl *ritual_ZNK28QWebEngineContextMenuRequest11referrerUrlEv(
    const QWebEngineContextMenuRequest *self) {
  return new QUrl(self->referrerUrl());
}

//  QtWebEngineCore::ReferrerPolicy
//      QWebEngineContextMenuRequest::referrerPolicy() const
extern "C" Q_DECL_EXPORT
QtWebEngineCore::ReferrerPolicy ritual_ZNK28QWebEngineContextMenuRequest14referrerPolicyEv(
    const QWebEngineContextMenuRequest *self) {
  return self->referrerPolicy();
}

//  bool QWebEngineContextMenuRequest::hasImageContent() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK28QWebEngineContextMenuRequest15hasImageContentEv(
    const QWebEngineContextMenuRequest *self) {
  return self->hasImageContent();
}

//  QString QWebEngineContextMenuRequest::suggestedFileName() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK28QWebEngineContextMenuRequest17suggestedFileNameEv(
    const QWebEngineContextMenuRequest *self) {
  return new QString(self->suggestedFileName());
}

//  QWebEngineContextMenuRequest::QWebEngineContextMenuRequest(QWebEngineCont
//      extMenuRequestPrivate *d)
extern "C" Q_DECL_EXPORT
QWebEngineContextMenuRequest *ritual_ZN28QWebEngineContextMenuRequestC1EP35QWebEngineContextMenuRequestPrivate(
    QWebEngineContextMenuRequestPrivate *d) {
  return new CuteQWebEngineContextMenuRequest(d);
}

//  a Python function taken by a CuteQWebEngineContextMenuRequest, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWebEngineContextMenuRequest(
    QWebEngineContextMenuRequest *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWebEngineContextMenuRequest *>(self)->take(key, call);
}
