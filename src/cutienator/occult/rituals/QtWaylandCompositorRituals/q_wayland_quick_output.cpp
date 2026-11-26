//  Written by dev_tooling.RitualGenerator from the records of
//  QtWaylandCompositor/qwaylandquickoutput.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtWaylandCompositor/qtwaylandcompositorglobal.h>
#if QT_CONFIG(wayland_compositor_quick)
#if QT_CONFIG(wayland_compositor_quick)
#include <QtWaylandCompositor/qwaylandquickoutput.h>
#include <QtCore/qstring.h>
#include <QtCore/qpoint.h>
#include <QtQml/QQmlListProperty>
#include <QtCore/QObject>

//  Only a class built on QWaylandQuickOutput may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQWaylandQuickOutput : QWaylandQuickOutput {
  using QWaylandQuickOutput::initialize;
  using QWaylandQuickOutput::classBegin;
  using QWaylandQuickOutput::componentComplete;
};

//  const QMetaObject *QWaylandQuickOutput::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK19QWaylandQuickOutput10metaObjectEv(
    const QWaylandQuickOutput *self) {
  return self->metaObject();
}

//  void *QWaylandQuickOutput::qt_metacast(const char *a0)
extern "C" Q_DECL_EXPORT
void *ritual_ZN19QWaylandQuickOutput11qt_metacastEPKc(
    QWaylandQuickOutput *self,
    const char *a0) {
  return self->qt_metacast(a0);
}

//  int QWaylandQuickOutput::qt_metacall(QMetaObject::Call a0, int a1, void
//      **a2)
extern "C" Q_DECL_EXPORT
int ritual_ZN19QWaylandQuickOutput11qt_metacallEN11QMetaObject4CallEiPPv(
    QWaylandQuickOutput *self,
    QMetaObject::Call a0,
    int a1,
    void **a2) {
  return self->qt_metacall(a0, a1, a2);
}

//  QString QWaylandQuickOutput::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN19QWaylandQuickOutput2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QWaylandQuickOutput::tr(s, c, n));
}

//  QQmlListProperty<QObject> QWaylandQuickOutput::data()
extern "C" Q_DECL_EXPORT
QQmlListProperty<QObject> *ritual_ZN19QWaylandQuickOutput4dataEv(
    QWaylandQuickOutput *self) {
  return new QQmlListProperty<QObject>(self->data());
}

//  void QWaylandQuickOutput::appendFunction(QQmlListProperty<QObject> *list,
//      QObject *object)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput14appendFunctionEP16QQmlListPropertyI7QObjectEPS1_(
    QQmlListProperty<QObject> *list,
    QObject *object) {
  QWaylandQuickOutput::appendFunction(list, object);
}

//  qsizetype QWaylandQuickOutput::countFunction(QQmlListProperty<QObject>
//      *list)
extern "C" Q_DECL_EXPORT
qsizetype ritual_ZN19QWaylandQuickOutput13countFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  return QWaylandQuickOutput::countFunction(list);
}

//  QObject *QWaylandQuickOutput::atFunction(QQmlListProperty<QObject> *list,
//      qsizetype index)
extern "C" Q_DECL_EXPORT
QObject *ritual_ZN19QWaylandQuickOutput10atFunctionEP16QQmlListPropertyI7QObjectEx(
    QQmlListProperty<QObject> *list,
    qsizetype index) {
  return QWaylandQuickOutput::atFunction(list, index);
}

//  void QWaylandQuickOutput::clearFunction(QQmlListProperty<QObject> *list)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput13clearFunctionEP16QQmlListPropertyI7QObjectE(
    QQmlListProperty<QObject> *list) {
  QWaylandQuickOutput::clearFunction(list);
}

//  QWaylandQuickOutput::QWaylandQuickOutput()
extern "C" Q_DECL_EXPORT
QWaylandQuickOutput *ritual_ZN19QWaylandQuickOutputC1Ev() {
  return new QWaylandQuickOutput();
}

//  QWaylandQuickOutput::QWaylandQuickOutput(QWaylandCompositor *compositor,
//      QWindow *window)
extern "C" Q_DECL_EXPORT
QWaylandQuickOutput *ritual_ZN19QWaylandQuickOutputC1EP18QWaylandCompositorP7QWindow(
    QWaylandCompositor *compositor,
    QWindow *window) {
  return new QWaylandQuickOutput(compositor, window);
}

//  void QWaylandQuickOutput::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput6updateEv(QWaylandQuickOutput *self) {
  self->update();
}

//  bool QWaylandQuickOutput::automaticFrameCallback() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QWaylandQuickOutput22automaticFrameCallbackEv(
    const QWaylandQuickOutput *self) {
  return self->automaticFrameCallback();
}

//  void QWaylandQuickOutput::setAutomaticFrameCallback(bool automatic)
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput25setAutomaticFrameCallbackEb(
    QWaylandQuickOutput *self,
    bool automatic) {
  self->setAutomaticFrameCallback(automatic);
}

//  QQuickItem *QWaylandQuickOutput::pickClickableItem(const QPointF
//      &position)
extern "C" Q_DECL_EXPORT
QQuickItem *ritual_ZN19QWaylandQuickOutput17pickClickableItemERK7QPointF(
    QWaylandQuickOutput *self,
    const QPointF *position) {
  return self->pickClickableItem(*position);
}

//  void QWaylandQuickOutput::updateStarted()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput13updateStartedEv(
    QWaylandQuickOutput *self) {
  self->updateStarted();
}

//  void QWaylandQuickOutput::automaticFrameCallbackChanged()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput29automaticFrameCallbackChangedEv(
    QWaylandQuickOutput *self) {
  self->automaticFrameCallbackChanged();
}

//  void QWaylandQuickOutput::initialize()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput10initializeEv(
    QWaylandQuickOutput *self) {
  self->initialize();
}

//  void QWaylandQuickOutput::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput10classBeginEv(
    QWaylandQuickOutput *self) {
  self->classBegin();
}

//  void QWaylandQuickOutput::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput17componentCompleteEv(
    QWaylandQuickOutput *self) {
  self->componentComplete();
}

//  void QWaylandQuickOutput::doFrameCallbacks()
extern "C" Q_DECL_EXPORT
void ritual_ZN19QWaylandQuickOutput16doFrameCallbacksEv(
    QWaylandQuickOutput *self) {
  self->doFrameCallbacks();
}

//  QWaylandQuickOutput as the QQmlParserStatus it is built on
extern "C" Q_DECL_EXPORT
QQmlParserStatus *ritual_cast_QWaylandQuickOutput_QQmlParserStatus(
    QWaylandQuickOutput *self) {
  return static_cast<QQmlParserStatus *>(self);
}

//  void QWaylandQuickOutput::update()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QWaylandQuickOutput6updateEv(QWaylandQuickOutput *self) {
  self->QWaylandQuickOutput::update();
}

//  void QWaylandQuickOutput::initialize()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QWaylandQuickOutput10initializeEv(
    QWaylandQuickOutput *self) {
  static_cast<OwnQWaylandQuickOutput *>(self)->OwnQWaylandQuickOutput::initialize();
}

//  void QWaylandQuickOutput::classBegin()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QWaylandQuickOutput10classBeginEv(
    QWaylandQuickOutput *self) {
  static_cast<OwnQWaylandQuickOutput *>(self)->OwnQWaylandQuickOutput::classBegin();
}

//  void QWaylandQuickOutput::componentComplete()
extern "C" Q_DECL_EXPORT
void ritual_own_ZN19QWaylandQuickOutput17componentCompleteEv(
    QWaylandQuickOutput *self) {
  static_cast<OwnQWaylandQuickOutput *>(self)->OwnQWaylandQuickOutput::componentComplete();
}

//  a QQmlListProperty<QObject> a ritual of QWaylandQuickOutput gave
extern "C" Q_DECL_EXPORT
void ritual_drop_QWaylandQuickOutput__QQmlListProperty_QObject(
    QQmlListProperty<QObject> *self) {
  delete self;
}

#endif  // QT_CONFIG(wayland_compositor_quick)
#endif  // QT_CONFIG(wayland_compositor_quick)
