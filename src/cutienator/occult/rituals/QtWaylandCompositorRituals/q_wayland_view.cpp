//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandview.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtWaylandCompositor/qwaylandview.h>
#include <QtCore/qstring.h>
#include <QtWaylandCompositor/qwaylandbufferref.h>
#include <QtGui/qregion.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QWaylandView that Python can take functions over in. Every QWaylandView
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQWaylandViewCall0)(const void *, const QWaylandBufferRef *, const QRegion *, int *);
typedef bool (*CuteQWaylandViewCall1)(const void *, int *);
typedef void (*CuteQWaylandViewCall2)(const void *, int *);
typedef const QWaylandBufferRef * (*CuteQWaylandViewCall3)(const void *, int *);
typedef const QRegion * (*CuteQWaylandViewCall4)(const void *, int *);
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandViewCall5)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQWaylandViewCall6)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandViewCall7)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandViewCall8)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandViewCall9)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandViewCall10)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQWaylandViewCall11)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQWaylandView : public QWaylandView {
public:
  using QWaylandView::QWaylandView;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN12QWaylandView15bufferCommittedERK17QWaylandBufferRefRK7QRegion")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QWaylandView7advanceEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QWaylandView20discardCurrentBufferEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QWaylandView13currentBufferEv")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN12QWaylandView13currentDamageEv")) {
      taken[4] = call;
      return true;
    }
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[5] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[6] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[7] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[8] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[9] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[10] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[11] = call;
      return true;
    }
#endif  // !defined(QT_NO_QOBJECT)
    return false;
  }

  //  void QWaylandView::bufferCommitted(const QWaylandBufferRef &buffer,
  //      const QRegion &damage)
  void bufferCommitted(
      const QWaylandBufferRef &buffer,
      const QRegion &damage) override {
    if (taken[0]) {
      int handled = 0;
      CuteQWaylandViewCall0 call = reinterpret_cast<CuteQWaylandViewCall0>(taken[0]);
      call(this, &buffer, &damage, &handled);
      if (handled) return;
    }
    QWaylandView::bufferCommitted(buffer, damage);
  }

  //  bool QWaylandView::advance()
  bool advance() override {
    if (taken[1]) {
      int handled = 0;
      CuteQWaylandViewCall1 call = reinterpret_cast<CuteQWaylandViewCall1>(taken[1]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QWaylandView::advance();
  }

  //  void QWaylandView::discardCurrentBuffer()
  void discardCurrentBuffer() override {
    if (taken[2]) {
      int handled = 0;
      CuteQWaylandViewCall2 call = reinterpret_cast<CuteQWaylandViewCall2>(taken[2]);
      call(this, &handled);
      if (handled) return;
    }
    QWaylandView::discardCurrentBuffer();
  }

  //  QWaylandBufferRef QWaylandView::currentBuffer()
  QWaylandBufferRef currentBuffer() override {
    if (taken[3]) {
      int handled = 0;
      CuteQWaylandViewCall3 call = reinterpret_cast<CuteQWaylandViewCall3>(taken[3]);
      const QWaylandBufferRef * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWaylandView::currentBuffer();
  }

  //  QRegion QWaylandView::currentDamage()
  QRegion currentDamage() override {
    if (taken[4]) {
      int handled = 0;
      CuteQWaylandViewCall4 call = reinterpret_cast<CuteQWaylandViewCall4>(taken[4]);
      const QRegion * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QWaylandView::currentDamage();
  }

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQWaylandViewCall5 call = reinterpret_cast<CuteQWaylandViewCall5>(taken[5]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QObject::event(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  bool QObject::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQWaylandViewCall6 call = reinterpret_cast<CuteQWaylandViewCall6>(taken[6]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QObject::eventFilter(watched, event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQWaylandViewCall7 call = reinterpret_cast<CuteQWaylandViewCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQWaylandViewCall8 call = reinterpret_cast<CuteQWaylandViewCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQWaylandViewCall9 call = reinterpret_cast<CuteQWaylandViewCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[10]) {
      int handled = 0;
      CuteQWaylandViewCall10 call = reinterpret_cast<CuteQWaylandViewCall10>(taken[10]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)

#if !defined(QT_NO_QOBJECT)
  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[11]) {
      int handled = 0;
      CuteQWaylandViewCall11 call = reinterpret_cast<CuteQWaylandViewCall11>(taken[11]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QWaylandView::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK12QWaylandView10metaObjectEv(
    const QWaylandView *self) {
  return self->metaObject();
}

//  void *QWaylandView::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN12QWaylandView11qt_metacastEPKc(
    QWaylandView *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandView::qt_metacall(QMetaObject::Call a0, int a1, void **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN12QWaylandView11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandView *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandView::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN12QWaylandView2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandView::tr(s, c, n));
}

//  QWaylandViewPrivate *QWaylandView::d_func()
extern "C" Q_DECL_EXPORT
QWaylandViewPrivate *ritual_ZN12QWaylandView6d_funcEv(QWaylandView *self) {
  return self->d_func();
}

//  const QWaylandViewPrivate *QWaylandView::d_func() const
extern "C" Q_DECL_EXPORT
const QWaylandViewPrivate *ritual_ZNK12QWaylandView6d_funcEv(
    const QWaylandView *self) {
  return self->d_func();
}

//  QWaylandView::QWaylandView(QObject *renderObject, QObject *parent)
extern "C" Q_DECL_EXPORT
QWaylandView *ritual_ZN12QWaylandViewC1EP7QObjectS1_(
    QObject *renderObject,
    QObject *parent) {
  return new CuteQWaylandView(renderObject, parent);
}

//  QWaylandView::~QWaylandView()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandViewD1Ev(QWaylandView *self) {
  delete self;
}

//  QObject *QWaylandView::renderObject() const
extern "C" Q_DECL_EXPORT
QObject *ritual_ZNK12QWaylandView12renderObjectEv(const QWaylandView *self) {
  return self->renderObject();
}

//  QWaylandSurface *QWaylandView::surface() const
extern "C" Q_DECL_EXPORT
QWaylandSurface *ritual_ZNK12QWaylandView7surfaceEv(
    const QWaylandView *self) {
  return self->surface();
}

//  void QWaylandView::setSurface(QWaylandSurface *surface)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView10setSurfaceEP15QWaylandSurface(
    QWaylandView *self,
    QWaylandSurface *surface) {
  self->setSurface(surface);
}

//  QWaylandOutput *QWaylandView::output() const
extern "C" Q_DECL_EXPORT
QWaylandOutput *ritual_ZNK12QWaylandView6outputEv(const QWaylandView *self) {
  return self->output();
}

//  void QWaylandView::setOutput(QWaylandOutput *output)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView9setOutputEP14QWaylandOutput(
    QWaylandView *self,
    QWaylandOutput *output) {
  self->setOutput(output);
}

//  void QWaylandView::bufferCommitted(const QWaylandBufferRef &buffer, const
//      QRegion &damage)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView15bufferCommittedERK17QWaylandBufferRefRK7QRegion(
    QWaylandView *self,
    const QWaylandBufferRef *buffer,
    const QRegion *damage) {
  self->bufferCommitted(*buffer, *damage);
}

//  bool QWaylandView::advance()
extern "C" Q_DECL_EXPORT
bool ritual_ZN12QWaylandView7advanceEv(QWaylandView *self) {
  return self->advance();
}

//  void QWaylandView::discardCurrentBuffer()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView20discardCurrentBufferEv(QWaylandView *self) {
  self->discardCurrentBuffer();
}

//  QWaylandBufferRef QWaylandView::currentBuffer()
extern "C" Q_DECL_EXPORT
QWaylandBufferRef *ritual_ZN12QWaylandView13currentBufferEv(
    QWaylandView *self) {
  return new QWaylandBufferRef(self->currentBuffer());
}

//  QRegion QWaylandView::currentDamage()
extern "C" Q_DECL_EXPORT
QRegion *ritual_ZN12QWaylandView13currentDamageEv(QWaylandView *self) {
  return new QRegion(self->currentDamage());
}

//  bool QWaylandView::isBufferLocked() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QWaylandView14isBufferLockedEv(const QWaylandView *self) {
  return self->isBufferLocked();
}

//  void QWaylandView::setBufferLocked(bool locked)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView15setBufferLockedEb(
    QWaylandView *self,
    bool locked) {
  self->setBufferLocked(locked);
}

//  bool QWaylandView::allowDiscardFrontBuffer() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QWaylandView23allowDiscardFrontBufferEv(
    const QWaylandView *self) {
  return self->allowDiscardFrontBuffer();
}

//  void QWaylandView::setAllowDiscardFrontBuffer(bool discard)
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView26setAllowDiscardFrontBufferEb(
    QWaylandView *self,
    bool discard) {
  self->setAllowDiscardFrontBuffer(discard);
}

//  void QWaylandView::setPrimary()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView10setPrimaryEv(QWaylandView *self) {
  self->setPrimary();
}

//  bool QWaylandView::isPrimary() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK12QWaylandView9isPrimaryEv(const QWaylandView *self) {
  return self->isPrimary();
}

//  struct wl_resource *QWaylandView::surfaceResource() const
extern "C" Q_DECL_EXPORT
struct wl_resource *ritual_ZNK12QWaylandView15surfaceResourceEv(
    const QWaylandView *self) {
  return self->surfaceResource();
}

//  void QWaylandView::surfaceChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView14surfaceChangedEv(QWaylandView *self) {
  self->surfaceChanged();
}

//  void QWaylandView::surfaceDestroyed()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView16surfaceDestroyedEv(QWaylandView *self) {
  self->surfaceDestroyed();
}

//  void QWaylandView::outputChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView13outputChangedEv(QWaylandView *self) {
  self->outputChanged();
}

//  void QWaylandView::bufferLockedChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView19bufferLockedChangedEv(QWaylandView *self) {
  self->bufferLockedChanged();
}

//  void QWaylandView::allowDiscardFrontBufferChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN12QWaylandView30allowDiscardFrontBufferChangedEv(
    QWaylandView *self) {
  self->allowDiscardFrontBufferChanged();
}

//  a Python function taken by a CuteQWaylandView, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QWaylandView(
    QWaylandView *self,
    const char *key,
    void *call) {
  return static_cast<CuteQWaylandView *>(self)->take(key, call);
}

//  void QWaylandView::bufferCommitted(const QWaylandBufferRef &buffer, const
//      QRegion &damage)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QWaylandView15bufferCommittedERK17QWaylandBufferRefRK7QRegion(
    QWaylandView *self,
    const QWaylandBufferRef *buffer,
    const QRegion *damage) {
  self->QWaylandView::bufferCommitted(*buffer, *damage);
}

//  bool QWaylandView::advance()
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN12QWaylandView7advanceEv(QWaylandView *self) {
  return self->QWaylandView::advance();
}

//  void QWaylandView::discardCurrentBuffer()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN12QWaylandView20discardCurrentBufferEv(
    QWaylandView *self) {
  self->QWaylandView::discardCurrentBuffer();
}

//  QWaylandBufferRef QWaylandView::currentBuffer()
extern "C" Q_DECL_EXPORT
QWaylandBufferRef *ritual_own_ZN12QWaylandView13currentBufferEv(
    QWaylandView *self) {
  return new QWaylandBufferRef(self->QWaylandView::currentBuffer());
}

//  QRegion QWaylandView::currentDamage()
extern "C" Q_DECL_EXPORT
QRegion *ritual_own_ZN12QWaylandView13currentDamageEv(QWaylandView *self) {
  return new QRegion(self->QWaylandView::currentDamage());
}

//  QList<QWaylandView *>::QList()
extern "C" Q_DECL_EXPORT
QList<QWaylandView *> *ritual_list_make_QWaylandView_ptr() {
  return new QList<QWaylandView *>();
}

//  void QList<QWaylandView *>::append(const QWaylandView * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QWaylandView_ptr(
    QList<QWaylandView *> *self,
    QWaylandView *element) {
  self->append(element);
}

//  qsizetype QList<QWaylandView *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QWaylandView_ptr(
    const QList<QWaylandView *> *self) {
  return self->size();
}

//  const QWaylandView * &QList<QWaylandView *>::at(qsizetype i) const
extern "C" Q_DECL_EXPORT
QWaylandView *ritual_list_at_QWaylandView_ptr(
    const QList<QWaylandView *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QWaylandView *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QWaylandView_ptr(QList<QWaylandView *> *self) {
  delete self;
}
