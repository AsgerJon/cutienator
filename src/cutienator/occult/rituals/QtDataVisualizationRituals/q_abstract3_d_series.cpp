//  Written by dev_tooling.RitualGenerator from the records of
//  QtDataVisualization/qabstract3dseries.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtDataVisualization/qabstract3dseries.h>
#include <QtCore/qstring.h>
#include <QtGui/qquaternion.h>
#include <QtGui/qvectornd.h>
#include <QtGui/qcolor.h>
#include <QtGui/qbrush.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A QAbstract3DSeries that Python can take functions over in. Every QAbstract3DSeries
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DSeriesCall0)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef bool (*CuteQAbstract3DSeriesCall1)(const void *, QObject *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesCall2)(const void *, QTimerEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesCall3)(const void *, QChildEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesCall4)(const void *, QEvent *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesCall5)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
#if !defined(QT_NO_QOBJECT)
typedef void (*CuteQAbstract3DSeriesCall6)(const void *, const QMetaMethod *, int *);
#endif  // !defined(QT_NO_QOBJECT)
class CuteQAbstract3DSeries : public QAbstract3DSeries {
public:
  using QAbstract3DSeries::QAbstract3DSeries;
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
      CuteQAbstract3DSeriesCall0 call = reinterpret_cast<CuteQAbstract3DSeriesCall0>(taken[0]);
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
      CuteQAbstract3DSeriesCall1 call = reinterpret_cast<CuteQAbstract3DSeriesCall1>(taken[1]);
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
      CuteQAbstract3DSeriesCall2 call = reinterpret_cast<CuteQAbstract3DSeriesCall2>(taken[2]);
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
      CuteQAbstract3DSeriesCall3 call = reinterpret_cast<CuteQAbstract3DSeriesCall3>(taken[3]);
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
      CuteQAbstract3DSeriesCall4 call = reinterpret_cast<CuteQAbstract3DSeriesCall4>(taken[4]);
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
      CuteQAbstract3DSeriesCall5 call = reinterpret_cast<CuteQAbstract3DSeriesCall5>(taken[5]);
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
      CuteQAbstract3DSeriesCall6 call = reinterpret_cast<CuteQAbstract3DSeriesCall6>(taken[6]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
#endif  // !defined(QT_NO_QOBJECT)
};

//  const QMetaObject *QAbstract3DSeries::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK17QAbstract3DSeries10metaObjectEv(
    const QAbstract3DSeries *self) {
  return self->metaObject();
}

//  QString QAbstract3DSeries::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN17QAbstract3DSeries2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QAbstract3DSeries::tr(s, c, n));
}

//  QAbstract3DSeries::QAbstract3DSeries(QAbstract3DSeriesPrivate *d, QObject
//      *parent)
extern "C" Q_DECL_EXPORT
QAbstract3DSeries *ritual_ZN17QAbstract3DSeriesC1EP24QAbstract3DSeriesPrivateP7QObject(
    QAbstract3DSeriesPrivate *d,
    QObject *parent) {
  return new CuteQAbstract3DSeries(d, parent);
}

//  QAbstract3DSeries::~QAbstract3DSeries()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeriesD1Ev(QAbstract3DSeries *self) {
  delete self;
}

//  SeriesType QAbstract3DSeries::type() const
extern "C" Q_DECL_EXPORT
QAbstract3DSeries::SeriesType ritual_ZNK17QAbstract3DSeries4typeEv(
    const QAbstract3DSeries *self) {
  return self->type();
}

//  void QAbstract3DSeries::setItemLabelFormat(const QString &format)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries18setItemLabelFormatERK7QString(
    QAbstract3DSeries *self,
    const QString *format) {
  self->setItemLabelFormat(*format);
}

//  QString QAbstract3DSeries::itemLabelFormat() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QAbstract3DSeries15itemLabelFormatEv(
    const QAbstract3DSeries *self) {
  return new QString(self->itemLabelFormat());
}

//  void QAbstract3DSeries::setVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries10setVisibleEb(
    QAbstract3DSeries *self,
    bool visible) {
  self->setVisible(visible);
}

//  bool QAbstract3DSeries::isVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstract3DSeries9isVisibleEv(
    const QAbstract3DSeries *self) {
  return self->isVisible();
}

//  void QAbstract3DSeries::setMesh(Mesh mesh)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries7setMeshENS_4MeshE(
    QAbstract3DSeries *self,
    QAbstract3DSeries::Mesh mesh) {
  self->setMesh(mesh);
}

//  Mesh QAbstract3DSeries::mesh() const
extern "C" Q_DECL_EXPORT
QAbstract3DSeries::Mesh ritual_ZNK17QAbstract3DSeries4meshEv(
    const QAbstract3DSeries *self) {
  return self->mesh();
}

//  void QAbstract3DSeries::setMeshSmooth(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries13setMeshSmoothEb(
    QAbstract3DSeries *self,
    bool enable) {
  self->setMeshSmooth(enable);
}

//  bool QAbstract3DSeries::isMeshSmooth() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstract3DSeries12isMeshSmoothEv(
    const QAbstract3DSeries *self) {
  return self->isMeshSmooth();
}

//  void QAbstract3DSeries::setMeshRotation(const QQuaternion &rotation)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries15setMeshRotationERK11QQuaternion(
    QAbstract3DSeries *self,
    const QQuaternion *rotation) {
  self->setMeshRotation(*rotation);
}

//  QQuaternion QAbstract3DSeries::meshRotation() const
extern "C" Q_DECL_EXPORT
QQuaternion *ritual_ZNK17QAbstract3DSeries12meshRotationEv(
    const QAbstract3DSeries *self) {
  return new QQuaternion(self->meshRotation());
}

//  void QAbstract3DSeries::setMeshAxisAndAngle(const QVector3D &axis, float
//      angle)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries19setMeshAxisAndAngleERK9QVector3Df(
    QAbstract3DSeries *self,
    const QVector3D *axis,
    float angle) {
  self->setMeshAxisAndAngle(*axis, angle);
}

//  void QAbstract3DSeries::setUserDefinedMesh(const QString &fileName)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries18setUserDefinedMeshERK7QString(
    QAbstract3DSeries *self,
    const QString *fileName) {
  self->setUserDefinedMesh(*fileName);
}

//  QString QAbstract3DSeries::userDefinedMesh() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QAbstract3DSeries15userDefinedMeshEv(
    const QAbstract3DSeries *self) {
  return new QString(self->userDefinedMesh());
}

//  void QAbstract3DSeries::setColorStyle(Q3DTheme::ColorStyle style)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries13setColorStyleEN8Q3DTheme10ColorStyleE(
    QAbstract3DSeries *self,
    Q3DTheme::ColorStyle style) {
  self->setColorStyle(style);
}

//  Q3DTheme::ColorStyle QAbstract3DSeries::colorStyle() const
extern "C" Q_DECL_EXPORT
Q3DTheme::ColorStyle ritual_ZNK17QAbstract3DSeries10colorStyleEv(
    const QAbstract3DSeries *self) {
  return self->colorStyle();
}

//  void QAbstract3DSeries::setBaseColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries12setBaseColorERK6QColor(
    QAbstract3DSeries *self,
    const QColor *color) {
  self->setBaseColor(*color);
}

//  QColor QAbstract3DSeries::baseColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QAbstract3DSeries9baseColorEv(
    const QAbstract3DSeries *self) {
  return new QColor(self->baseColor());
}

//  void QAbstract3DSeries::setBaseGradient(const QLinearGradient &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries15setBaseGradientERK15QLinearGradient(
    QAbstract3DSeries *self,
    const QLinearGradient *gradient) {
  self->setBaseGradient(*gradient);
}

//  QLinearGradient QAbstract3DSeries::baseGradient() const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZNK17QAbstract3DSeries12baseGradientEv(
    const QAbstract3DSeries *self) {
  return new QLinearGradient(self->baseGradient());
}

//  void QAbstract3DSeries::setSingleHighlightColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries23setSingleHighlightColorERK6QColor(
    QAbstract3DSeries *self,
    const QColor *color) {
  self->setSingleHighlightColor(*color);
}

//  QColor QAbstract3DSeries::singleHighlightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QAbstract3DSeries20singleHighlightColorEv(
    const QAbstract3DSeries *self) {
  return new QColor(self->singleHighlightColor());
}

//  void QAbstract3DSeries::setSingleHighlightGradient(const QLinearGradient
//      &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries26setSingleHighlightGradientERK15QLinearGradient(
    QAbstract3DSeries *self,
    const QLinearGradient *gradient) {
  self->setSingleHighlightGradient(*gradient);
}

//  QLinearGradient QAbstract3DSeries::singleHighlightGradient() const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZNK17QAbstract3DSeries23singleHighlightGradientEv(
    const QAbstract3DSeries *self) {
  return new QLinearGradient(self->singleHighlightGradient());
}

//  void QAbstract3DSeries::setMultiHighlightColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries22setMultiHighlightColorERK6QColor(
    QAbstract3DSeries *self,
    const QColor *color) {
  self->setMultiHighlightColor(*color);
}

//  QColor QAbstract3DSeries::multiHighlightColor() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK17QAbstract3DSeries19multiHighlightColorEv(
    const QAbstract3DSeries *self) {
  return new QColor(self->multiHighlightColor());
}

//  void QAbstract3DSeries::setMultiHighlightGradient(const QLinearGradient
//      &gradient)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries25setMultiHighlightGradientERK15QLinearGradient(
    QAbstract3DSeries *self,
    const QLinearGradient *gradient) {
  self->setMultiHighlightGradient(*gradient);
}

//  QLinearGradient QAbstract3DSeries::multiHighlightGradient() const
extern "C" Q_DECL_EXPORT
QLinearGradient *ritual_ZNK17QAbstract3DSeries22multiHighlightGradientEv(
    const QAbstract3DSeries *self) {
  return new QLinearGradient(self->multiHighlightGradient());
}

//  void QAbstract3DSeries::setName(const QString &name)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries7setNameERK7QString(
    QAbstract3DSeries *self,
    const QString *name) {
  self->setName(*name);
}

//  QString QAbstract3DSeries::name() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QAbstract3DSeries4nameEv(
    const QAbstract3DSeries *self) {
  return new QString(self->name());
}

//  QString QAbstract3DSeries::itemLabel() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QAbstract3DSeries9itemLabelEv(
    const QAbstract3DSeries *self) {
  return new QString(self->itemLabel());
}

//  void QAbstract3DSeries::setItemLabelVisible(bool visible)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QAbstract3DSeries19setItemLabelVisibleEb(
    QAbstract3DSeries *self,
    bool visible) {
  self->setItemLabelVisible(visible);
}

//  bool QAbstract3DSeries::isItemLabelVisible() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QAbstract3DSeries18isItemLabelVisibleEv(
    const QAbstract3DSeries *self) {
  return self->isItemLabelVisible();
}

//  a Python function taken by a CuteQAbstract3DSeries, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QAbstract3DSeries(
    QAbstract3DSeries *self,
    const char *key,
    void *call) {
  return static_cast<CuteQAbstract3DSeries *>(self)->take(key, call);
}

//  QList<QAbstract3DSeries *>::QList()
extern "C" Q_DECL_EXPORT
QList<QAbstract3DSeries *> *ritual_list_make_QAbstract3DSeries_ptr() {
  return new QList<QAbstract3DSeries *>();
}

//  void QList<QAbstract3DSeries *>::append(const QAbstract3DSeries * &value)
extern "C" Q_DECL_EXPORT
void ritual_list_add_QAbstract3DSeries_ptr(
    QList<QAbstract3DSeries *> *self,
    QAbstract3DSeries *element) {
  self->append(element);
}

//  qsizetype QList<QAbstract3DSeries *>::size() const
extern "C" Q_DECL_EXPORT
long long ritual_list_size_QAbstract3DSeries_ptr(
    const QList<QAbstract3DSeries *> *self) {
  return self->size();
}

//  const QAbstract3DSeries * &QList<QAbstract3DSeries *>::at(qsizetype i)
//      const
extern "C" Q_DECL_EXPORT
QAbstract3DSeries *ritual_list_at_QAbstract3DSeries_ptr(
    const QList<QAbstract3DSeries *> *self,
    long long index) {
  return self->at(index);
}

//  QList<QAbstract3DSeries *>::~QList()
extern "C" Q_DECL_EXPORT
void ritual_list_drop_QAbstract3DSeries_ptr(
    QList<QAbstract3DSeries *> *self) {
  delete self;
}
