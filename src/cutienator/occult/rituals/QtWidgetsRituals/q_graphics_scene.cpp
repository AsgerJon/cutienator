//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/qgraphicsscene.h, Qt 6.12.0. Changes made here are lost.
#include <QtWidgets/qgraphicsscene.h>
#include <QtCore/qstring.h>
#include <QtCore/qrect.h>
#include <QtWidgets/qgraphicsitem.h>
#include <QtCore/qpoint.h>
#include <QtGui/qtransform.h>
#include <QtGui/qpolygon.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpen.h>
#include <QtGui/qbrush.h>
#include <QtCore/qline.h>
#include <QtGui/qpixmap.h>
#include <QtGui/qfont.h>
#include <QtCore/qvariant.h>
#include <QtWidgets/qgraphicsview.h>
#include <QtGui/qpalette.h>
#include <QtCore/qmetaobject.h>
#include <QtCore/qlist.h>
#include <cstring>

//  Only a class built on QGraphicsScene may call these functions of it.
//  This one is, and makes them free for the rituals to call.
struct OwnQGraphicsScene : QGraphicsScene {
  using QGraphicsScene::event;
  using QGraphicsScene::eventFilter;
  using QGraphicsScene::contextMenuEvent;
  using QGraphicsScene::dragEnterEvent;
  using QGraphicsScene::dragMoveEvent;
  using QGraphicsScene::dragLeaveEvent;
  using QGraphicsScene::dropEvent;
  using QGraphicsScene::focusInEvent;
  using QGraphicsScene::focusOutEvent;
  using QGraphicsScene::helpEvent;
  using QGraphicsScene::keyPressEvent;
  using QGraphicsScene::keyReleaseEvent;
  using QGraphicsScene::mousePressEvent;
  using QGraphicsScene::mouseMoveEvent;
  using QGraphicsScene::mouseReleaseEvent;
  using QGraphicsScene::mouseDoubleClickEvent;
  using QGraphicsScene::wheelEvent;
  using QGraphicsScene::inputMethodEvent;
  using QGraphicsScene::drawBackground;
  using QGraphicsScene::drawForeground;
  using QGraphicsScene::focusNextPrevChild;
};

//  A QGraphicsScene that Python can take functions over in. Every QGraphicsScene
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef const QVariant * (*CuteQGraphicsSceneCall0)(const void *, int, int *);
typedef bool (*CuteQGraphicsSceneCall1)(const void *, QEvent *, int *);
typedef bool (*CuteQGraphicsSceneCall2)(const void *, QObject *, QEvent *, int *);
typedef void (*CuteQGraphicsSceneCall3)(const void *, QGraphicsSceneContextMenuEvent *, int *);
typedef void (*CuteQGraphicsSceneCall4)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsSceneCall5)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsSceneCall6)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsSceneCall7)(const void *, QGraphicsSceneDragDropEvent *, int *);
typedef void (*CuteQGraphicsSceneCall8)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsSceneCall9)(const void *, QFocusEvent *, int *);
typedef void (*CuteQGraphicsSceneCall10)(const void *, QGraphicsSceneHelpEvent *, int *);
typedef void (*CuteQGraphicsSceneCall11)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsSceneCall12)(const void *, QKeyEvent *, int *);
typedef void (*CuteQGraphicsSceneCall13)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsSceneCall14)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsSceneCall15)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsSceneCall16)(const void *, QGraphicsSceneMouseEvent *, int *);
typedef void (*CuteQGraphicsSceneCall17)(const void *, QGraphicsSceneWheelEvent *, int *);
typedef void (*CuteQGraphicsSceneCall18)(const void *, QInputMethodEvent *, int *);
typedef void (*CuteQGraphicsSceneCall19)(const void *, QPainter *, const QRectF *, int *);
typedef void (*CuteQGraphicsSceneCall20)(const void *, QPainter *, const QRectF *, int *);
typedef bool (*CuteQGraphicsSceneCall21)(const void *, bool, int *);
typedef void (*CuteQGraphicsSceneCall22)(const void *, QTimerEvent *, int *);
typedef void (*CuteQGraphicsSceneCall23)(const void *, QChildEvent *, int *);
typedef void (*CuteQGraphicsSceneCall24)(const void *, QEvent *, int *);
typedef void (*CuteQGraphicsSceneCall25)(const void *, const QMetaMethod *, int *);
typedef void (*CuteQGraphicsSceneCall26)(const void *, const QMetaMethod *, int *);
class CuteQGraphicsScene : public QGraphicsScene {
public:
  using QGraphicsScene::QGraphicsScene;
  void *taken[27] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZNK14QGraphicsScene16inputMethodQueryEN2Qt16InputMethodQueryE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject5eventEP6QEvent")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11eventFilterEPS_P6QEvent")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene16contextMenuEventEP30QGraphicsSceneContextMenuEvent")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene14dragEnterEventEP27QGraphicsSceneDragDropEvent")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene13dragMoveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene14dragLeaveEventEP27QGraphicsSceneDragDropEvent")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene9dropEventEP27QGraphicsSceneDragDropEvent")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene12focusInEventEP11QFocusEvent")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene13focusOutEventEP11QFocusEvent")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene9helpEventEP23QGraphicsSceneHelpEvent")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene13keyPressEventEP9QKeyEvent")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene15keyReleaseEventEP9QKeyEvent")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene15mousePressEventEP24QGraphicsSceneMouseEvent")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene14mouseMoveEventEP24QGraphicsSceneMouseEvent")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene17mouseReleaseEventEP24QGraphicsSceneMouseEvent")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene10wheelEventEP24QGraphicsSceneWheelEvent")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene16inputMethodEventEP17QInputMethodEvent")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene14drawBackgroundEP8QPainterRK6QRectF")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene14drawForegroundEP8QPainterRK6QRectF")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN14QGraphicsScene18focusNextPrevChildEb")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10timerEventEP11QTimerEvent")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject10childEventEP11QChildEvent")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject11customEventEP6QEvent")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject13connectNotifyERK11QMetaMethod")) {
      taken[25] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QObject16disconnectNotifyERK11QMetaMethod")) {
      taken[26] = call;
      return true;
    }
    return false;
  }

  //  QVariant QGraphicsScene::inputMethodQuery(Qt::InputMethodQuery query)
  //      const
  QVariant inputMethodQuery(Qt::InputMethodQuery query) const override {
    if (taken[0]) {
      int handled = 0;
      CuteQGraphicsSceneCall0 call = reinterpret_cast<CuteQGraphicsSceneCall0>(taken[0]);
      const QVariant * given = call(this, static_cast<int>(query), &handled);
      if (handled && given) return *given;
    }
    return QGraphicsScene::inputMethodQuery(query);
  }

  //  bool QGraphicsScene::event(QEvent *event)
  bool event(QEvent *event) override {
    if (taken[1]) {
      int handled = 0;
      CuteQGraphicsSceneCall1 call = reinterpret_cast<CuteQGraphicsSceneCall1>(taken[1]);
      bool given = call(this, event, &handled);
      if (handled) return given;
    }
    return QGraphicsScene::event(event);
  }

  //  bool QGraphicsScene::eventFilter(QObject *watched, QEvent *event)
  bool eventFilter(QObject *watched, QEvent *event) override {
    if (taken[2]) {
      int handled = 0;
      CuteQGraphicsSceneCall2 call = reinterpret_cast<CuteQGraphicsSceneCall2>(taken[2]);
      bool given = call(this, watched, event, &handled);
      if (handled) return given;
    }
    return QGraphicsScene::eventFilter(watched, event);
  }

  //  void QGraphicsScene::contextMenuEvent(QGraphicsSceneContextMenuEvent
  //      *event)
  void contextMenuEvent(QGraphicsSceneContextMenuEvent *event) override {
    if (taken[3]) {
      int handled = 0;
      CuteQGraphicsSceneCall3 call = reinterpret_cast<CuteQGraphicsSceneCall3>(taken[3]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::contextMenuEvent(event);
  }

  //  void QGraphicsScene::dragEnterEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragEnterEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[4]) {
      int handled = 0;
      CuteQGraphicsSceneCall4 call = reinterpret_cast<CuteQGraphicsSceneCall4>(taken[4]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::dragEnterEvent(event);
  }

  //  void QGraphicsScene::dragMoveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragMoveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[5]) {
      int handled = 0;
      CuteQGraphicsSceneCall5 call = reinterpret_cast<CuteQGraphicsSceneCall5>(taken[5]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::dragMoveEvent(event);
  }

  //  void QGraphicsScene::dragLeaveEvent(QGraphicsSceneDragDropEvent
  //      *event)
  void dragLeaveEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[6]) {
      int handled = 0;
      CuteQGraphicsSceneCall6 call = reinterpret_cast<CuteQGraphicsSceneCall6>(taken[6]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::dragLeaveEvent(event);
  }

  //  void QGraphicsScene::dropEvent(QGraphicsSceneDragDropEvent *event)
  void dropEvent(QGraphicsSceneDragDropEvent *event) override {
    if (taken[7]) {
      int handled = 0;
      CuteQGraphicsSceneCall7 call = reinterpret_cast<CuteQGraphicsSceneCall7>(taken[7]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::dropEvent(event);
  }

  //  void QGraphicsScene::focusInEvent(QFocusEvent *event)
  void focusInEvent(QFocusEvent *event) override {
    if (taken[8]) {
      int handled = 0;
      CuteQGraphicsSceneCall8 call = reinterpret_cast<CuteQGraphicsSceneCall8>(taken[8]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::focusInEvent(event);
  }

  //  void QGraphicsScene::focusOutEvent(QFocusEvent *event)
  void focusOutEvent(QFocusEvent *event) override {
    if (taken[9]) {
      int handled = 0;
      CuteQGraphicsSceneCall9 call = reinterpret_cast<CuteQGraphicsSceneCall9>(taken[9]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::focusOutEvent(event);
  }

  //  void QGraphicsScene::helpEvent(QGraphicsSceneHelpEvent *event)
  void helpEvent(QGraphicsSceneHelpEvent *event) override {
    if (taken[10]) {
      int handled = 0;
      CuteQGraphicsSceneCall10 call = reinterpret_cast<CuteQGraphicsSceneCall10>(taken[10]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::helpEvent(event);
  }

  //  void QGraphicsScene::keyPressEvent(QKeyEvent *event)
  void keyPressEvent(QKeyEvent *event) override {
    if (taken[11]) {
      int handled = 0;
      CuteQGraphicsSceneCall11 call = reinterpret_cast<CuteQGraphicsSceneCall11>(taken[11]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::keyPressEvent(event);
  }

  //  void QGraphicsScene::keyReleaseEvent(QKeyEvent *event)
  void keyReleaseEvent(QKeyEvent *event) override {
    if (taken[12]) {
      int handled = 0;
      CuteQGraphicsSceneCall12 call = reinterpret_cast<CuteQGraphicsSceneCall12>(taken[12]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::keyReleaseEvent(event);
  }

  //  void QGraphicsScene::mousePressEvent(QGraphicsSceneMouseEvent *event)
  void mousePressEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[13]) {
      int handled = 0;
      CuteQGraphicsSceneCall13 call = reinterpret_cast<CuteQGraphicsSceneCall13>(taken[13]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::mousePressEvent(event);
  }

  //  void QGraphicsScene::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
  void mouseMoveEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[14]) {
      int handled = 0;
      CuteQGraphicsSceneCall14 call = reinterpret_cast<CuteQGraphicsSceneCall14>(taken[14]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::mouseMoveEvent(event);
  }

  //  void QGraphicsScene::mouseReleaseEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseReleaseEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[15]) {
      int handled = 0;
      CuteQGraphicsSceneCall15 call = reinterpret_cast<CuteQGraphicsSceneCall15>(taken[15]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::mouseReleaseEvent(event);
  }

  //  void QGraphicsScene::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
  //      *event)
  void mouseDoubleClickEvent(QGraphicsSceneMouseEvent *event) override {
    if (taken[16]) {
      int handled = 0;
      CuteQGraphicsSceneCall16 call = reinterpret_cast<CuteQGraphicsSceneCall16>(taken[16]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::mouseDoubleClickEvent(event);
  }

  //  void QGraphicsScene::wheelEvent(QGraphicsSceneWheelEvent *event)
  void wheelEvent(QGraphicsSceneWheelEvent *event) override {
    if (taken[17]) {
      int handled = 0;
      CuteQGraphicsSceneCall17 call = reinterpret_cast<CuteQGraphicsSceneCall17>(taken[17]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::wheelEvent(event);
  }

  //  void QGraphicsScene::inputMethodEvent(QInputMethodEvent *event)
  void inputMethodEvent(QInputMethodEvent *event) override {
    if (taken[18]) {
      int handled = 0;
      CuteQGraphicsSceneCall18 call = reinterpret_cast<CuteQGraphicsSceneCall18>(taken[18]);
      call(this, event, &handled);
      if (handled) return;
    }
    QGraphicsScene::inputMethodEvent(event);
  }

  //  void QGraphicsScene::drawBackground(QPainter *painter, const QRectF
  //      &rect)
  void drawBackground(QPainter *painter, const QRectF &rect) override {
    if (taken[19]) {
      int handled = 0;
      CuteQGraphicsSceneCall19 call = reinterpret_cast<CuteQGraphicsSceneCall19>(taken[19]);
      call(this, painter, &rect, &handled);
      if (handled) return;
    }
    QGraphicsScene::drawBackground(painter, rect);
  }

  //  void QGraphicsScene::drawForeground(QPainter *painter, const QRectF
  //      &rect)
  void drawForeground(QPainter *painter, const QRectF &rect) override {
    if (taken[20]) {
      int handled = 0;
      CuteQGraphicsSceneCall20 call = reinterpret_cast<CuteQGraphicsSceneCall20>(taken[20]);
      call(this, painter, &rect, &handled);
      if (handled) return;
    }
    QGraphicsScene::drawForeground(painter, rect);
  }

  //  bool QGraphicsScene::focusNextPrevChild(bool next)
  bool focusNextPrevChild(bool next) override {
    if (taken[21]) {
      int handled = 0;
      CuteQGraphicsSceneCall21 call = reinterpret_cast<CuteQGraphicsSceneCall21>(taken[21]);
      bool given = call(this, next, &handled);
      if (handled) return given;
    }
    return QGraphicsScene::focusNextPrevChild(next);
  }

  //  void QObject::timerEvent(QTimerEvent *event)
  void timerEvent(QTimerEvent *event) override {
    if (taken[22]) {
      int handled = 0;
      CuteQGraphicsSceneCall22 call = reinterpret_cast<CuteQGraphicsSceneCall22>(taken[22]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::timerEvent(event);
  }

  //  void QObject::childEvent(QChildEvent *event)
  void childEvent(QChildEvent *event) override {
    if (taken[23]) {
      int handled = 0;
      CuteQGraphicsSceneCall23 call = reinterpret_cast<CuteQGraphicsSceneCall23>(taken[23]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::childEvent(event);
  }

  //  void QObject::customEvent(QEvent *event)
  void customEvent(QEvent *event) override {
    if (taken[24]) {
      int handled = 0;
      CuteQGraphicsSceneCall24 call = reinterpret_cast<CuteQGraphicsSceneCall24>(taken[24]);
      call(this, event, &handled);
      if (handled) return;
    }
    QObject::customEvent(event);
  }

  //  void QObject::connectNotify(const QMetaMethod &signal)
  void connectNotify(const QMetaMethod &signal) override {
    if (taken[25]) {
      int handled = 0;
      CuteQGraphicsSceneCall25 call = reinterpret_cast<CuteQGraphicsSceneCall25>(taken[25]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::connectNotify(signal);
  }

  //  void QObject::disconnectNotify(const QMetaMethod &signal)
  void disconnectNotify(const QMetaMethod &signal) override {
    if (taken[26]) {
      int handled = 0;
      CuteQGraphicsSceneCall26 call = reinterpret_cast<CuteQGraphicsSceneCall26>(taken[26]);
      call(this, &signal, &handled);
      if (handled) return;
    }
    QObject::disconnectNotify(signal);
  }
};

//  const QMetaObject *QGraphicsScene::metaObject() const
extern "C" Q_DECL_EXPORT
const QMetaObject *ritual_ZNK14QGraphicsScene10metaObjectEv(
    const QGraphicsScene *self) {
  return self->metaObject();
}

//  QString QGraphicsScene::tr(const char *s, const char *c, int n)
extern "C" Q_DECL_EXPORT
QString *ritual_ZN14QGraphicsScene2trEPKcS1_i(
    const char *s,
    const char *c,
    int n) {
  return new QString(QGraphicsScene::tr(s, c, n));
}

//  QGraphicsScene::QGraphicsScene(QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZN14QGraphicsSceneC1EP7QObject(QObject *parent) {
  return new CuteQGraphicsScene(parent);
}

//  QGraphicsScene::QGraphicsScene(const QRectF &sceneRect, QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZN14QGraphicsSceneC1ERK6QRectFP7QObject(
    const QRectF *sceneRect,
    QObject *parent) {
  return new CuteQGraphicsScene(*sceneRect, parent);
}

//  QGraphicsScene::QGraphicsScene(qreal x, qreal y, qreal width, qreal
//      height, QObject *parent)
extern "C" Q_DECL_EXPORT
QGraphicsScene *ritual_ZN14QGraphicsSceneC1EddddP7QObject(
    qreal x,
    qreal y,
    qreal width,
    qreal height,
    QObject *parent) {
  return new CuteQGraphicsScene(x, y, width, height, parent);
}

//  QGraphicsScene::~QGraphicsScene()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsSceneD1Ev(QGraphicsScene *self) {
  delete self;
}

//  QRectF QGraphicsScene::sceneRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QGraphicsScene9sceneRectEv(const QGraphicsScene *self) {
  return new QRectF(self->sceneRect());
}

//  qreal QGraphicsScene::width() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScene5widthEv(const QGraphicsScene *self) {
  return self->width();
}

//  qreal QGraphicsScene::height() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScene6heightEv(const QGraphicsScene *self) {
  return self->height();
}

//  void QGraphicsScene::setSceneRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene12setSceneRectERK6QRectF(
    QGraphicsScene *self,
    const QRectF *rect) {
  self->setSceneRect(*rect);
}

//  void QGraphicsScene::setSceneRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene12setSceneRectEdddd(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setSceneRect(x, y, w, h);
}

//  void QGraphicsScene::render(QPainter *painter, const QRectF &target,
//      const QRectF &source, Qt::AspectRatioMode aspectRatioMode)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene6renderEP8QPainterRK6QRectFS4_N2Qt15AspectRatioModeE(
    QGraphicsScene *self,
    QPainter *painter,
    const QRectF *target,
    const QRectF *source,
    Qt::AspectRatioMode aspectRatioMode) {
  self->render(painter, *target, *source, aspectRatioMode);
}

//  ItemIndexMethod QGraphicsScene::itemIndexMethod() const
extern "C" Q_DECL_EXPORT
QGraphicsScene::ItemIndexMethod ritual_ZNK14QGraphicsScene15itemIndexMethodEv(
    const QGraphicsScene *self) {
  return self->itemIndexMethod();
}

//  void QGraphicsScene::setItemIndexMethod(ItemIndexMethod method)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene18setItemIndexMethodENS_15ItemIndexMethodE(
    QGraphicsScene *self,
    QGraphicsScene::ItemIndexMethod method) {
  self->setItemIndexMethod(method);
}

//  int QGraphicsScene::bspTreeDepth() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK14QGraphicsScene12bspTreeDepthEv(const QGraphicsScene *self) {
  return self->bspTreeDepth();
}

//  void QGraphicsScene::setBspTreeDepth(int depth)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene15setBspTreeDepthEi(
    QGraphicsScene *self,
    int depth) {
  self->setBspTreeDepth(depth);
}

//  QRectF QGraphicsScene::itemsBoundingRect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK14QGraphicsScene17itemsBoundingRectEv(
    const QGraphicsScene *self) {
  return new QRectF(self->itemsBoundingRect());
}

//  QList<QGraphicsItem *> QGraphicsScene::items(Qt::SortOrder order) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK14QGraphicsScene5itemsEN2Qt9SortOrderE(
    const QGraphicsScene *self,
    Qt::SortOrder order) {
  return new QList<QGraphicsItem *>(self->items(order));
}

//  QList<QGraphicsItem *> QGraphicsScene::items(const QPointF &pos,
//      Qt::ItemSelectionMode mode, Qt::SortOrder order, const QTransform
//      &deviceTransform) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK14QGraphicsScene5itemsERK7QPointFN2Qt17ItemSelectionModeENS3_9SortOrderERK10QTransform(
    const QGraphicsScene *self,
    const QPointF *pos,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const QTransform *deviceTransform) {
  return new QList<QGraphicsItem *>(
      self->items(
          *pos,
          mode,
          order,
          *deviceTransform));
}

//  QList<QGraphicsItem *> QGraphicsScene::items(const QRectF &rect,
//      Qt::ItemSelectionMode mode, Qt::SortOrder order, const QTransform
//      &deviceTransform) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK14QGraphicsScene5itemsERK6QRectFN2Qt17ItemSelectionModeENS3_9SortOrderERK10QTransform(
    const QGraphicsScene *self,
    const QRectF *rect,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const QTransform *deviceTransform) {
  return new QList<QGraphicsItem *>(
      self->items(
          *rect,
          mode,
          order,
          *deviceTransform));
}

//  QList<QGraphicsItem *> QGraphicsScene::items(const QPolygonF &polygon,
//      Qt::ItemSelectionMode mode, Qt::SortOrder order, const QTransform
//      &deviceTransform) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK14QGraphicsScene5itemsERK9QPolygonFN2Qt17ItemSelectionModeENS3_9SortOrderERK10QTransform(
    const QGraphicsScene *self,
    const QPolygonF *polygon,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const QTransform *deviceTransform) {
  return new QList<QGraphicsItem *>(
      self->items(
          *polygon,
          mode,
          order,
          *deviceTransform));
}

//  QList<QGraphicsItem *> QGraphicsScene::items(const QPainterPath &path,
//      Qt::ItemSelectionMode mode, Qt::SortOrder order, const QTransform
//      &deviceTransform) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK14QGraphicsScene5itemsERK12QPainterPathN2Qt17ItemSelectionModeENS3_9SortOrderERK10QTransform(
    const QGraphicsScene *self,
    const QPainterPath *path,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const QTransform *deviceTransform) {
  return new QList<QGraphicsItem *>(
      self->items(
          *path,
          mode,
          order,
          *deviceTransform));
}

//  QList<QGraphicsItem *> QGraphicsScene::items(qreal x, qreal y, qreal w,
//      qreal h, Qt::ItemSelectionMode mode, Qt::SortOrder order, const
//      QTransform &deviceTransform) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK14QGraphicsScene5itemsEddddN2Qt17ItemSelectionModeENS0_9SortOrderERK10QTransform(
    const QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    Qt::ItemSelectionMode mode,
    Qt::SortOrder order,
    const QTransform *deviceTransform) {
  return new QList<QGraphicsItem *>(
      self->items(
          x,
          y,
          w,
          h,
          mode,
          order,
          *deviceTransform));
}

//  QList<QGraphicsItem *> QGraphicsScene::collidingItems(const QGraphicsItem
//      *item, Qt::ItemSelectionMode mode) const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK14QGraphicsScene14collidingItemsEPK13QGraphicsItemN2Qt17ItemSelectionModeE(
    const QGraphicsScene *self,
    const QGraphicsItem *item,
    Qt::ItemSelectionMode mode) {
  return new QList<QGraphicsItem *>(self->collidingItems(item, mode));
}

//  QGraphicsItem *QGraphicsScene::itemAt(const QPointF &pos, const
//      QTransform &deviceTransform) const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene6itemAtERK7QPointFRK10QTransform(
    const QGraphicsScene *self,
    const QPointF *pos,
    const QTransform *deviceTransform) {
  return self->itemAt(*pos, *deviceTransform);
}

//  QGraphicsItem *QGraphicsScene::itemAt(qreal x, qreal y, const QTransform
//      &deviceTransform) const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene6itemAtEddRK10QTransform(
    const QGraphicsScene *self,
    qreal x,
    qreal y,
    const QTransform *deviceTransform) {
  return self->itemAt(x, y, *deviceTransform);
}

//  QList<QGraphicsItem *> QGraphicsScene::selectedItems() const
extern "C" Q_DECL_EXPORT
QList<QGraphicsItem *> *ritual_ZNK14QGraphicsScene13selectedItemsEv(
    const QGraphicsScene *self) {
  return new QList<QGraphicsItem *>(self->selectedItems());
}

//  QPainterPath QGraphicsScene::selectionArea() const
extern "C" Q_DECL_EXPORT
QPainterPath *ritual_ZNK14QGraphicsScene13selectionAreaEv(
    const QGraphicsScene *self) {
  return new QPainterPath(self->selectionArea());
}

//  void QGraphicsScene::setSelectionArea(const QPainterPath &path, const
//      QTransform &deviceTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene16setSelectionAreaERK12QPainterPathRK10QTransform(
    QGraphicsScene *self,
    const QPainterPath *path,
    const QTransform *deviceTransform) {
  self->setSelectionArea(*path, *deviceTransform);
}

//  void QGraphicsScene::setSelectionArea(const QPainterPath &path,
//      Qt::ItemSelectionOperation selectionOperation, Qt::ItemSelectionMode
//      mode, const QTransform &deviceTransform)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene16setSelectionAreaERK12QPainterPathN2Qt22ItemSelectionOperationENS3_17ItemSelectionModeERK10QTransform(
    QGraphicsScene *self,
    const QPainterPath *path,
    Qt::ItemSelectionOperation selectionOperation,
    Qt::ItemSelectionMode mode,
    const QTransform *deviceTransform) {
  self->setSelectionArea(*path, selectionOperation, mode, *deviceTransform);
}

//  QGraphicsItemGroup *QGraphicsScene::createItemGroup(const
//      QList<QGraphicsItem *> &items)
extern "C" Q_DECL_EXPORT
QGraphicsItemGroup *ritual_ZN14QGraphicsScene15createItemGroupERK5QListIP13QGraphicsItemE(
    QGraphicsScene *self,
    const QList<QGraphicsItem *> *items) {
  return self->createItemGroup(*items);
}

//  void QGraphicsScene::destroyItemGroup(QGraphicsItemGroup *group)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene16destroyItemGroupEP18QGraphicsItemGroup(
    QGraphicsScene *self,
    QGraphicsItemGroup *group) {
  self->destroyItemGroup(group);
}

//  void QGraphicsScene::addItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene7addItemEP13QGraphicsItem(
    QGraphicsScene *self,
    QGraphicsItem *item) {
  self->addItem(item);
}

//  QGraphicsEllipseItem *QGraphicsScene::addEllipse(const QRectF &rect,
//      const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsEllipseItem *ritual_ZN14QGraphicsScene10addEllipseERK6QRectFRK4QPenRK6QBrush(
    QGraphicsScene *self,
    const QRectF *rect,
    const QPen *pen,
    const QBrush *brush) {
  return self->addEllipse(*rect, *pen, *brush);
}

//  QGraphicsLineItem *QGraphicsScene::addLine(const QLineF &line, const QPen
//      &pen)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN14QGraphicsScene7addLineERK6QLineFRK4QPen(
    QGraphicsScene *self,
    const QLineF *line,
    const QPen *pen) {
  return self->addLine(*line, *pen);
}

//  QGraphicsPathItem *QGraphicsScene::addPath(const QPainterPath &path,
//      const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsPathItem *ritual_ZN14QGraphicsScene7addPathERK12QPainterPathRK4QPenRK6QBrush(
    QGraphicsScene *self,
    const QPainterPath *path,
    const QPen *pen,
    const QBrush *brush) {
  return self->addPath(*path, *pen, *brush);
}

//  QGraphicsPixmapItem *QGraphicsScene::addPixmap(const QPixmap &pixmap)
extern "C" Q_DECL_EXPORT
QGraphicsPixmapItem *ritual_ZN14QGraphicsScene9addPixmapERK7QPixmap(
    QGraphicsScene *self,
    const QPixmap *pixmap) {
  return self->addPixmap(*pixmap);
}

//  QGraphicsPolygonItem *QGraphicsScene::addPolygon(const QPolygonF
//      &polygon, const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsPolygonItem *ritual_ZN14QGraphicsScene10addPolygonERK9QPolygonFRK4QPenRK6QBrush(
    QGraphicsScene *self,
    const QPolygonF *polygon,
    const QPen *pen,
    const QBrush *brush) {
  return self->addPolygon(*polygon, *pen, *brush);
}

//  QGraphicsRectItem *QGraphicsScene::addRect(const QRectF &rect, const QPen
//      &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN14QGraphicsScene7addRectERK6QRectFRK4QPenRK6QBrush(
    QGraphicsScene *self,
    const QRectF *rect,
    const QPen *pen,
    const QBrush *brush) {
  return self->addRect(*rect, *pen, *brush);
}

//  QGraphicsTextItem *QGraphicsScene::addText(const QString &text, const
//      QFont &font)
extern "C" Q_DECL_EXPORT
QGraphicsTextItem *ritual_ZN14QGraphicsScene7addTextERK7QStringRK5QFont(
    QGraphicsScene *self,
    const QString *text,
    const QFont *font) {
  return self->addText(*text, *font);
}

//  QGraphicsSimpleTextItem *QGraphicsScene::addSimpleText(const QString
//      &text, const QFont &font)
extern "C" Q_DECL_EXPORT
QGraphicsSimpleTextItem *ritual_ZN14QGraphicsScene13addSimpleTextERK7QStringRK5QFont(
    QGraphicsScene *self,
    const QString *text,
    const QFont *font) {
  return self->addSimpleText(*text, *font);
}

//  QGraphicsProxyWidget *QGraphicsScene::addWidget(QWidget *widget,
//      Qt::WindowFlags wFlags)
extern "C" Q_DECL_EXPORT
QGraphicsProxyWidget *ritual_ZN14QGraphicsScene9addWidgetEP7QWidget6QFlagsIN2Qt10WindowTypeEE(
    QGraphicsScene *self,
    QWidget *widget,
    int wFlags) {
  return self->addWidget(widget, QFlags<Qt::WindowType>::fromInt(wFlags));
}

//  QGraphicsEllipseItem *QGraphicsScene::addEllipse(qreal x, qreal y, qreal
//      w, qreal h, const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsEllipseItem *ritual_ZN14QGraphicsScene10addEllipseEddddRK4QPenRK6QBrush(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    const QPen *pen,
    const QBrush *brush) {
  return self->addEllipse(x, y, w, h, *pen, *brush);
}

//  QGraphicsLineItem *QGraphicsScene::addLine(qreal x1, qreal y1, qreal x2,
//      qreal y2, const QPen &pen)
extern "C" Q_DECL_EXPORT
QGraphicsLineItem *ritual_ZN14QGraphicsScene7addLineEddddRK4QPen(
    QGraphicsScene *self,
    qreal x1,
    qreal y1,
    qreal x2,
    qreal y2,
    const QPen *pen) {
  return self->addLine(x1, y1, x2, y2, *pen);
}

//  QGraphicsRectItem *QGraphicsScene::addRect(qreal x, qreal y, qreal w,
//      qreal h, const QPen &pen, const QBrush &brush)
extern "C" Q_DECL_EXPORT
QGraphicsRectItem *ritual_ZN14QGraphicsScene7addRectEddddRK4QPenRK6QBrush(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    const QPen *pen,
    const QBrush *brush) {
  return self->addRect(x, y, w, h, *pen, *brush);
}

//  void QGraphicsScene::removeItem(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10removeItemEP13QGraphicsItem(
    QGraphicsScene *self,
    QGraphicsItem *item) {
  self->removeItem(item);
}

//  QGraphicsItem *QGraphicsScene::focusItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene9focusItemEv(
    const QGraphicsScene *self) {
  return self->focusItem();
}

//  void QGraphicsScene::setFocusItem(QGraphicsItem *item, Qt::FocusReason
//      focusReason)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene12setFocusItemEP13QGraphicsItemN2Qt11FocusReasonE(
    QGraphicsScene *self,
    QGraphicsItem *item,
    Qt::FocusReason focusReason) {
  self->setFocusItem(item, focusReason);
}

//  bool QGraphicsScene::hasFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGraphicsScene8hasFocusEv(const QGraphicsScene *self) {
  return self->hasFocus();
}

//  void QGraphicsScene::setFocus(Qt::FocusReason focusReason)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene8setFocusEN2Qt11FocusReasonE(
    QGraphicsScene *self,
    Qt::FocusReason focusReason) {
  self->setFocus(focusReason);
}

//  void QGraphicsScene::clearFocus()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10clearFocusEv(QGraphicsScene *self) {
  self->clearFocus();
}

//  void QGraphicsScene::setStickyFocus(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14setStickyFocusEb(
    QGraphicsScene *self,
    bool enabled) {
  self->setStickyFocus(enabled);
}

//  bool QGraphicsScene::stickyFocus() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGraphicsScene11stickyFocusEv(const QGraphicsScene *self) {
  return self->stickyFocus();
}

//  QGraphicsItem *QGraphicsScene::mouseGrabberItem() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene16mouseGrabberItemEv(
    const QGraphicsScene *self) {
  return self->mouseGrabberItem();
}

//  QBrush QGraphicsScene::backgroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK14QGraphicsScene15backgroundBrushEv(
    const QGraphicsScene *self) {
  return new QBrush(self->backgroundBrush());
}

//  void QGraphicsScene::setBackgroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene18setBackgroundBrushERK6QBrush(
    QGraphicsScene *self,
    const QBrush *brush) {
  self->setBackgroundBrush(*brush);
}

//  QBrush QGraphicsScene::foregroundBrush() const
extern "C" Q_DECL_EXPORT
QBrush *ritual_ZNK14QGraphicsScene15foregroundBrushEv(
    const QGraphicsScene *self) {
  return new QBrush(self->foregroundBrush());
}

//  void QGraphicsScene::setForegroundBrush(const QBrush &brush)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene18setForegroundBrushERK6QBrush(
    QGraphicsScene *self,
    const QBrush *brush) {
  self->setForegroundBrush(*brush);
}

//  QVariant QGraphicsScene::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK14QGraphicsScene16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsScene *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->inputMethodQuery(query));
}

//  QList<QGraphicsView *> QGraphicsScene::views() const
extern "C" Q_DECL_EXPORT
QList<QGraphicsView *> *ritual_ZNK14QGraphicsScene5viewsEv(
    const QGraphicsScene *self) {
  return new QList<QGraphicsView *>(self->views());
}

//  void QGraphicsScene::update(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene6updateEdddd(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->update(x, y, w, h);
}

//  void QGraphicsScene::invalidate(qreal x, qreal y, qreal w, qreal h,
//      SceneLayers layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10invalidateEdddd6QFlagsINS_10SceneLayerEE(
    QGraphicsScene *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h,
    int layers) {
  self->invalidate(
      x,
      y,
      w,
      h,
      QFlags<QGraphicsScene::SceneLayer>::fromInt(layers));
}

//  QStyle *QGraphicsScene::style() const
extern "C" Q_DECL_EXPORT
QStyle *ritual_ZNK14QGraphicsScene5styleEv(const QGraphicsScene *self) {
  return self->style();
}

//  void QGraphicsScene::setStyle(QStyle *style)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene8setStyleEP6QStyle(
    QGraphicsScene *self,
    QStyle *style) {
  self->setStyle(style);
}

//  QFont QGraphicsScene::font() const
extern "C" Q_DECL_EXPORT
QFont *ritual_ZNK14QGraphicsScene4fontEv(const QGraphicsScene *self) {
  return new QFont(self->font());
}

//  void QGraphicsScene::setFont(const QFont &font)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene7setFontERK5QFont(
    QGraphicsScene *self,
    const QFont *font) {
  self->setFont(*font);
}

//  QPalette QGraphicsScene::palette() const
extern "C" Q_DECL_EXPORT
QPalette *ritual_ZNK14QGraphicsScene7paletteEv(const QGraphicsScene *self) {
  return new QPalette(self->palette());
}

//  void QGraphicsScene::setPalette(const QPalette &palette)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10setPaletteERK8QPalette(
    QGraphicsScene *self,
    const QPalette *palette) {
  self->setPalette(*palette);
}

//  bool QGraphicsScene::isActive() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGraphicsScene8isActiveEv(const QGraphicsScene *self) {
  return self->isActive();
}

//  QGraphicsItem *QGraphicsScene::activePanel() const
extern "C" Q_DECL_EXPORT
QGraphicsItem *ritual_ZNK14QGraphicsScene11activePanelEv(
    const QGraphicsScene *self) {
  return self->activePanel();
}

//  void QGraphicsScene::setActivePanel(QGraphicsItem *item)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14setActivePanelEP13QGraphicsItem(
    QGraphicsScene *self,
    QGraphicsItem *item) {
  self->setActivePanel(item);
}

//  QGraphicsWidget *QGraphicsScene::activeWindow() const
extern "C" Q_DECL_EXPORT
QGraphicsWidget *ritual_ZNK14QGraphicsScene12activeWindowEv(
    const QGraphicsScene *self) {
  return self->activeWindow();
}

//  void QGraphicsScene::setActiveWindow(QGraphicsWidget *widget)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene15setActiveWindowEP15QGraphicsWidget(
    QGraphicsScene *self,
    QGraphicsWidget *widget) {
  self->setActiveWindow(widget);
}

//  bool QGraphicsScene::sendEvent(QGraphicsItem *item, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QGraphicsScene9sendEventEP13QGraphicsItemP6QEvent(
    QGraphicsScene *self,
    QGraphicsItem *item,
    QEvent *event) {
  return self->sendEvent(item, event);
}

//  qreal QGraphicsScene::minimumRenderSize() const
extern "C" Q_DECL_EXPORT
qreal ritual_ZNK14QGraphicsScene17minimumRenderSizeEv(
    const QGraphicsScene *self) {
  return self->minimumRenderSize();
}

//  void QGraphicsScene::setMinimumRenderSize(qreal minSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene20setMinimumRenderSizeEd(
    QGraphicsScene *self,
    qreal minSize) {
  self->setMinimumRenderSize(minSize);
}

//  bool QGraphicsScene::focusOnTouch() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK14QGraphicsScene12focusOnTouchEv(const QGraphicsScene *self) {
  return self->focusOnTouch();
}

//  void QGraphicsScene::setFocusOnTouch(bool enabled)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene15setFocusOnTouchEb(
    QGraphicsScene *self,
    bool enabled) {
  self->setFocusOnTouch(enabled);
}

//  void QGraphicsScene::update(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene6updateERK6QRectF(
    QGraphicsScene *self,
    const QRectF *rect) {
  self->update(*rect);
}

//  void QGraphicsScene::invalidate(const QRectF &rect, SceneLayers layers)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10invalidateERK6QRectF6QFlagsINS_10SceneLayerEE(
    QGraphicsScene *self,
    const QRectF *rect,
    int layers) {
  self->invalidate(
      *rect,
      QFlags<QGraphicsScene::SceneLayer>::fromInt(layers));
}

//  void QGraphicsScene::advance()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene7advanceEv(QGraphicsScene *self) {
  self->advance();
}

//  void QGraphicsScene::clearSelection()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14clearSelectionEv(QGraphicsScene *self) {
  self->clearSelection();
}

//  void QGraphicsScene::clear()
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene5clearEv(QGraphicsScene *self) {
  self->clear();
}

//  bool QGraphicsScene::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QGraphicsScene5eventEP6QEvent(
    QGraphicsScene *self,
    QEvent *event) {
  return self->event(event);
}

//  bool QGraphicsScene::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QGraphicsScene11eventFilterEP7QObjectP6QEvent(
    QGraphicsScene *self,
    QObject *watched,
    QEvent *event) {
  return self->eventFilter(watched, event);
}

//  void QGraphicsScene::contextMenuEvent(QGraphicsSceneContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene16contextMenuEventEP30QGraphicsSceneContextMenuEvent(
    QGraphicsScene *self,
    QGraphicsSceneContextMenuEvent *event) {
  self->contextMenuEvent(event);
}

//  void QGraphicsScene::dragEnterEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14dragEnterEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsScene *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dragEnterEvent(event);
}

//  void QGraphicsScene::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene13dragMoveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsScene *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dragMoveEvent(event);
}

//  void QGraphicsScene::dragLeaveEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14dragLeaveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsScene *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dragLeaveEvent(event);
}

//  void QGraphicsScene::dropEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene9dropEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsScene *self,
    QGraphicsSceneDragDropEvent *event) {
  self->dropEvent(event);
}

//  void QGraphicsScene::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene12focusInEventEP11QFocusEvent(
    QGraphicsScene *self,
    QFocusEvent *event) {
  self->focusInEvent(event);
}

//  void QGraphicsScene::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene13focusOutEventEP11QFocusEvent(
    QGraphicsScene *self,
    QFocusEvent *event) {
  self->focusOutEvent(event);
}

//  void QGraphicsScene::helpEvent(QGraphicsSceneHelpEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene9helpEventEP23QGraphicsSceneHelpEvent(
    QGraphicsScene *self,
    QGraphicsSceneHelpEvent *event) {
  self->helpEvent(event);
}

//  void QGraphicsScene::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene13keyPressEventEP9QKeyEvent(
    QGraphicsScene *self,
    QKeyEvent *event) {
  self->keyPressEvent(event);
}

//  void QGraphicsScene::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene15keyReleaseEventEP9QKeyEvent(
    QGraphicsScene *self,
    QKeyEvent *event) {
  self->keyReleaseEvent(event);
}

//  void QGraphicsScene::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene15mousePressEventEP24QGraphicsSceneMouseEvent(
    QGraphicsScene *self,
    QGraphicsSceneMouseEvent *event) {
  self->mousePressEvent(event);
}

//  void QGraphicsScene::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14mouseMoveEventEP24QGraphicsSceneMouseEvent(
    QGraphicsScene *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseMoveEvent(event);
}

//  void QGraphicsScene::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    QGraphicsScene *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseReleaseEvent(event);
}

//  void QGraphicsScene::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    QGraphicsScene *self,
    QGraphicsSceneMouseEvent *event) {
  self->mouseDoubleClickEvent(event);
}

//  void QGraphicsScene::wheelEvent(QGraphicsSceneWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene10wheelEventEP24QGraphicsSceneWheelEvent(
    QGraphicsScene *self,
    QGraphicsSceneWheelEvent *event) {
  self->wheelEvent(event);
}

//  void QGraphicsScene::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene16inputMethodEventEP17QInputMethodEvent(
    QGraphicsScene *self,
    QInputMethodEvent *event) {
  self->inputMethodEvent(event);
}

//  void QGraphicsScene::drawBackground(QPainter *painter, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14drawBackgroundEP8QPainterRK6QRectF(
    QGraphicsScene *self,
    QPainter *painter,
    const QRectF *rect) {
  self->drawBackground(painter, *rect);
}

//  void QGraphicsScene::drawForeground(QPainter *painter, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN14QGraphicsScene14drawForegroundEP8QPainterRK6QRectF(
    QGraphicsScene *self,
    QPainter *painter,
    const QRectF *rect) {
  self->drawForeground(painter, *rect);
}

//  bool QGraphicsScene::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_ZN14QGraphicsScene18focusNextPrevChildEb(
    QGraphicsScene *self,
    bool next) {
  return self->focusNextPrevChild(next);
}

//  QGraphicsScenePrivate *QGraphicsScene::d_func()
extern "C" Q_DECL_EXPORT
QGraphicsScenePrivate *ritual_ZN14QGraphicsScene6d_funcEv(
    QGraphicsScene *self) {
  return self->d_func();
}

//  const QGraphicsScenePrivate *QGraphicsScene::d_func() const
extern "C" Q_DECL_EXPORT
const QGraphicsScenePrivate *ritual_ZNK14QGraphicsScene6d_funcEv(
    const QGraphicsScene *self) {
  return self->d_func();
}

//  a Python function taken by a CuteQGraphicsScene, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QGraphicsScene(
    QGraphicsScene *self,
    const char *key,
    void *call) {
  return static_cast<CuteQGraphicsScene *>(self)->take(key, call);
}

//  QVariant QGraphicsScene::inputMethodQuery(Qt::InputMethodQuery query)
//      const
extern "C" Q_DECL_EXPORT
QVariant *ritual_own_ZNK14QGraphicsScene16inputMethodQueryEN2Qt16InputMethodQueryE(
    const QGraphicsScene *self,
    Qt::InputMethodQuery query) {
  return new QVariant(self->QGraphicsScene::inputMethodQuery(query));
}

//  bool QGraphicsScene::event(QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QGraphicsScene5eventEP6QEvent(
    QGraphicsScene *self,
    QEvent *event) {
  return static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::event(
      event);
}

//  bool QGraphicsScene::eventFilter(QObject *watched, QEvent *event)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QGraphicsScene11eventFilterEP7QObjectP6QEvent(
    QGraphicsScene *self,
    QObject *watched,
    QEvent *event) {
  return static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::eventFilter(
      watched,
      event);
}

//  void QGraphicsScene::contextMenuEvent(QGraphicsSceneContextMenuEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene16contextMenuEventEP30QGraphicsSceneContextMenuEvent(
    QGraphicsScene *self,
    QGraphicsSceneContextMenuEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::contextMenuEvent(
      event);
}

//  void QGraphicsScene::dragEnterEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene14dragEnterEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsScene *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::dragEnterEvent(
      event);
}

//  void QGraphicsScene::dragMoveEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene13dragMoveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsScene *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::dragMoveEvent(
      event);
}

//  void QGraphicsScene::dragLeaveEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene14dragLeaveEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsScene *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::dragLeaveEvent(
      event);
}

//  void QGraphicsScene::dropEvent(QGraphicsSceneDragDropEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene9dropEventEP27QGraphicsSceneDragDropEvent(
    QGraphicsScene *self,
    QGraphicsSceneDragDropEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::dropEvent(
      event);
}

//  void QGraphicsScene::focusInEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene12focusInEventEP11QFocusEvent(
    QGraphicsScene *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::focusInEvent(
      event);
}

//  void QGraphicsScene::focusOutEvent(QFocusEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene13focusOutEventEP11QFocusEvent(
    QGraphicsScene *self,
    QFocusEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::focusOutEvent(
      event);
}

//  void QGraphicsScene::helpEvent(QGraphicsSceneHelpEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene9helpEventEP23QGraphicsSceneHelpEvent(
    QGraphicsScene *self,
    QGraphicsSceneHelpEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::helpEvent(
      event);
}

//  void QGraphicsScene::keyPressEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene13keyPressEventEP9QKeyEvent(
    QGraphicsScene *self,
    QKeyEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::keyPressEvent(
      event);
}

//  void QGraphicsScene::keyReleaseEvent(QKeyEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene15keyReleaseEventEP9QKeyEvent(
    QGraphicsScene *self,
    QKeyEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::keyReleaseEvent(
      event);
}

//  void QGraphicsScene::mousePressEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene15mousePressEventEP24QGraphicsSceneMouseEvent(
    QGraphicsScene *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::mousePressEvent(
      event);
}

//  void QGraphicsScene::mouseMoveEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene14mouseMoveEventEP24QGraphicsSceneMouseEvent(
    QGraphicsScene *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::mouseMoveEvent(
      event);
}

//  void QGraphicsScene::mouseReleaseEvent(QGraphicsSceneMouseEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene17mouseReleaseEventEP24QGraphicsSceneMouseEvent(
    QGraphicsScene *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::mouseReleaseEvent(
      event);
}

//  void QGraphicsScene::mouseDoubleClickEvent(QGraphicsSceneMouseEvent
//      *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene21mouseDoubleClickEventEP24QGraphicsSceneMouseEvent(
    QGraphicsScene *self,
    QGraphicsSceneMouseEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::mouseDoubleClickEvent(
      event);
}

//  void QGraphicsScene::wheelEvent(QGraphicsSceneWheelEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene10wheelEventEP24QGraphicsSceneWheelEvent(
    QGraphicsScene *self,
    QGraphicsSceneWheelEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::wheelEvent(
      event);
}

//  void QGraphicsScene::inputMethodEvent(QInputMethodEvent *event)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene16inputMethodEventEP17QInputMethodEvent(
    QGraphicsScene *self,
    QInputMethodEvent *event) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::inputMethodEvent(
      event);
}

//  void QGraphicsScene::drawBackground(QPainter *painter, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene14drawBackgroundEP8QPainterRK6QRectF(
    QGraphicsScene *self,
    QPainter *painter,
    const QRectF *rect) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::drawBackground(
      painter,
      *rect);
}

//  void QGraphicsScene::drawForeground(QPainter *painter, const QRectF
//      &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN14QGraphicsScene14drawForegroundEP8QPainterRK6QRectF(
    QGraphicsScene *self,
    QPainter *painter,
    const QRectF *rect) {
  static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::drawForeground(
      painter,
      *rect);
}

//  bool QGraphicsScene::focusNextPrevChild(bool next)
extern "C" Q_DECL_EXPORT
bool ritual_own_ZN14QGraphicsScene18focusNextPrevChildEb(
    QGraphicsScene *self,
    bool next) {
  return static_cast<OwnQGraphicsScene *>(self)->OwnQGraphicsScene::focusNextPrevChild(
      next);
}
