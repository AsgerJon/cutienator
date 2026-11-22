//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/qtextobject.h, Qt 6.12.0. Changes made here are lost.
#include <QtGui/qtextobject.h>
#include <QtCore/qstring.h>
#include <QtGui/qtextformat.h>
#include <QtGui/qtextcursor.h>
#include <QtCore/qmetaobject.h>
#include <cstring>

//  A QTextFrame that Python can take functions over in. Every QTextFrame
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef bool (*CuteQTextFrameCall0)(const void *, QEvent *, int *);
typedef bool (*CuteQTextFrameCall1)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQTextFrameCall2)(const void *, QTimerEvent *, int *);
typedef void (*CuteQTextFrameCall3)(const void *, QChildEvent *, int *);
typedef void (*CuteQTextFrameCall4)(const void *, QEvent *, int *);
typedef void (*CuteQTextFrameCall5)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQTextFrameCall6)(const void *, const QMetaMethod *, int *);
class CuteQTextFrame : public QTextFrame {
public:
  using QTextFrame::QTextFrame;
  void *taken[7] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[6] = call;
      return true;
    }
    return false;
  }

  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[0]) {
      int handled = 0;
      CuteQTextFrameCall0 call = reinterpret_cast<CuteQTextFrameCall0>(taken[0]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }

  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQTextFrameCall1 call = reinterpret_cast<CuteQTextFrameCall1>(taken[1]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQTextFrameCall2 call = reinterpret_cast<CuteQTextFrameCall2>(taken[2]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQTextFrameCall3 call = reinterpret_cast<CuteQTextFrameCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQTextFrameCall4 call = reinterpret_cast<CuteQTextFrameCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[5]) {
      int handled = 0;
      CuteQTextFrameCall5 call = reinterpret_cast<CuteQTextFrameCall5>(taken[5]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[6]) {
      int handled = 0;
      CuteQTextFrameCall6 call = reinterpret_cast<CuteQTextFrameCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QTextFrame::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK10QTextFrame10metaObjectEv(
    const QTextFrame *self) {
  return self->metaObject();
}

//  QString QTextFrame::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN10QTextFrame2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QTextFrame::tr(s, c, n));
}

//  QTextFrame::QTextFrame(QTextDocument *doc)
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZN10QTextFrameC1EP13QTextDocument(QTextDocument *doc) {
  return new CuteQTextFrame(doc);
}

//  QTextFrame::~QTextFrame()
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextFrameD1Ev(QTextFrame *self) {
  delete self;
}

//  void QTextFrame::setFrameFormat(const QTextFrameFormat &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextFrame14setFrameFormatERK16QTextFrameFormat(
    QTextFrame *self,
    const QTextFrameFormat *format) {
  self->setFrameFormat(*format);
}

//  QTextFrameFormat QTextFrame::frameFormat() const
extern "C" Q_DECL_EXPORT
QTextFrameFormat *ritual_ZNK10QTextFrame11frameFormatEv(
    const QTextFrame *self) {
  return new QTextFrameFormat(self->frameFormat());
}

//  QTextCursor QTextFrame::firstCursorPosition() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK10QTextFrame19firstCursorPositionEv(
    const QTextFrame *self) {
  return new QTextCursor(self->firstCursorPosition());
}

//  QTextCursor QTextFrame::lastCursorPosition() const
extern "C" Q_DECL_EXPORT
QTextCursor *ritual_ZNK10QTextFrame18lastCursorPositionEv(
    const QTextFrame *self) {
  return new QTextCursor(self->lastCursorPosition());
}

//  int QTextFrame::firstPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextFrame13firstPositionEv(const QTextFrame *self) {
  return self->firstPosition();
}

//  int QTextFrame::lastPosition() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK10QTextFrame12lastPositionEv(const QTextFrame *self) {
  return self->lastPosition();
}

//  QTextFrameLayoutData *QTextFrame::layoutData() const
extern "C" Q_DECL_EXPORT
QTextFrameLayoutData *ritual_ZNK10QTextFrame10layoutDataEv(
    const QTextFrame *self) {
  return self->layoutData();
}

//  void QTextFrame::setLayoutData(QTextFrameLayoutData *data)
extern "C" Q_DECL_EXPORT
void ritual_ZN10QTextFrame13setLayoutDataEP20QTextFrameLayoutData(
    QTextFrame *self,
    QTextFrameLayoutData *data) {
  self->setLayoutData(data);
}

//  QTextFrame *QTextFrame::parentFrame() const
extern "C" Q_DECL_EXPORT
QTextFrame *ritual_ZNK10QTextFrame11parentFrameEv(const QTextFrame *self) {
  return self->parentFrame();
}

//  iterator QTextFrame::begin() const
extern "C" Q_DECL_EXPORT
QTextFrame::iterator *ritual_ZNK10QTextFrame5beginEv(
    const QTextFrame *self) {
  return new QTextFrame::iterator(self->begin());
}

//  iterator QTextFrame::end() const
extern "C" Q_DECL_EXPORT
QTextFrame::iterator *ritual_ZNK10QTextFrame3endEv(const QTextFrame *self) {
  return new QTextFrame::iterator(self->end());
}

//  a Python function taken by a CuteQTextFrame, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QTextFrame(QTextFrame *self, const char *key, void *call) {
  return static_cast<CuteQTextFrame *>(self)->take(key, call);
}
