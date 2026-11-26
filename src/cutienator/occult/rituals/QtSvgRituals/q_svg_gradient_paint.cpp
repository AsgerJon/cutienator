//  Written by dev_tooling.RitualGenerator from the records of
//  QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtSvg/6.12.0/QtSvg/private/qtsvgglobal_p.h>
#include <QtSvg/QtSvg>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtSvg/6.12.0/QtSvg/private/qsvgpaintserver_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qstring.h>
#include <QtGui/qtransform.h>
#include <QtGui/qbrush.h>
#include <cstring>

//  A QSvgGradientPaint that Python can take functions over in. Every QSvgGradientPaint
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef int (*CuteQSvgGradientPaintCall0)(const void *, int *);
class CuteQSvgGradientPaint : public QSvgGradientPaint {
public:
  using QSvgGradientPaint::QSvgGradientPaint;
  void *taken[1] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK15QSvgPaintServer4typeEv")) {
      taken[0] = call;
      return true;
    }
    return false;
  }

  //  Type QSvgGradientPaint::type() const
  QSvgPaintServer::Type type() const override {
    if (taken[0]) {
      int handled = 0;
      CuteQSvgGradientPaintCall0 call = reinterpret_cast<CuteQSvgGradientPaintCall0>(taken[0]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSvgPaintServer::Type>(given);
    }
    return QSvgGradientPaint::type();
  }
};

//  QSvgGradientPaint::~QSvgGradientPaint()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgGradientPaintD1Ev(QSvgGradientPaint *self) {
  delete self;
}

//  Type QSvgGradientPaint::type() const
extern "C" Q_DECL_EXPORT
QSvgPaintServer::Type ritual_ZNK17QSvgGradientPaint4typeEv(
    const QSvgGradientPaint *self) {
  return self->type();
}

//  void QSvgGradientPaint::setStopLink(const QString &link, QSvgDocument
//      *doc)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgGradientPaint11setStopLinkERK7QStringP12QSvgDocument(
    QSvgGradientPaint *self,
    const QString *link,
    QSvgDocument *doc) {
  self->setStopLink(*link, doc);
}

//  QString QSvgGradientPaint::stopLink() const
extern "C" Q_DECL_EXPORT
QString *ritual_ZNK17QSvgGradientPaint8stopLinkEv(
    const QSvgGradientPaint *self) {
  return new QString(self->stopLink());
}

//  void QSvgGradientPaint::setTransform(const QTransform &transform)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgGradientPaint12setTransformERK10QTransform(
    QSvgGradientPaint *self,
    const QTransform *transform) {
  self->setTransform(*transform);
}

//  QTransform QSvgGradientPaint::qtransform() const
extern "C" Q_DECL_EXPORT
QTransform *ritual_ZNK17QSvgGradientPaint10qtransformEv(
    const QSvgGradientPaint *self) {
  return new QTransform(self->qtransform());
}

//  QGradient *QSvgGradientPaint::qgradient()
extern "C" Q_DECL_EXPORT
QGradient *ritual_ZN17QSvgGradientPaint9qgradientEv(
    QSvgGradientPaint *self) {
  return self->qgradient();
}

//  bool QSvgGradientPaint::gradientStopsSet() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK17QSvgGradientPaint16gradientStopsSetEv(
    const QSvgGradientPaint *self) {
  return self->gradientStopsSet();
}

//  void QSvgGradientPaint::setGradientStopsSet(bool set)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgGradientPaint19setGradientStopsSetEb(
    QSvgGradientPaint *self,
    bool set) {
  self->setGradientStopsSet(set);
}

//  QBrush QSvgGradientPaint::brush(QPainter *a0, const QSvgNode *a1,
//      QSvgExtraStates &a2)
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZN17QSvgGradientPaint5brushEP8QPainterPK8QSvgNodeR15QSvgExtraStates(
    QSvgGradientPaint *self,
    QPainter *a0,
    const QSvgNode *a1,
    QSvgExtraStates *a2) {
  return new QBrush(self->brush(a0, a1, *a2));
}

//  void QSvgGradientPaint::resolveStops()
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgGradientPaint12resolveStopsEv(QSvgGradientPaint *self) {
  self->resolveStops();
}

//  void QSvgGradientPaint::resolveStops_helper(QSet<QString> &visited)
extern "C" Q_DECL_EXPORT
void ritual_ZN17QSvgGradientPaint19resolveStops_helperER4QSetI7QStringE(
    QSvgGradientPaint *self,
    QSet<QString> *visited) {
  self->resolveStops_helper(*visited);
}

//  a Python function taken by a CuteQSvgGradientPaint, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSvgGradientPaint(
    QSvgGradientPaint *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSvgGradientPaint *>(self)->take(key, call);
}

//  Type QSvgGradientPaint::type() const
extern "C" Q_DECL_EXPORT
QSvgPaintServer::Type ritual_own_ZNK17QSvgGradientPaint4typeEv(
    const QSvgGradientPaint *self) {
  return self->QSvgGradientPaint::type();
}
