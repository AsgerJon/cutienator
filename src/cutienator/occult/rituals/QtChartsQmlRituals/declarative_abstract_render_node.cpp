//  Written by dev_tooling.RitualGenerator from the records of
//  QtChartsQml/6.12.0/QtChartsQml/private/declarativeabstractrendernode_p.h,
//  Qt 6.12.0. Changes made here are lost.
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativechartglobal_p.h>
#include <QtChartsQml/QtChartsQml>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtChartsQml/6.12.0/QtChartsQml/private/declarativeabstractrendernode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qsize.h>
#include <QtCore/qrect.h>
#include <QtGui/qevent.h>
#include <QtCore/qlist.h>
#include <cstring>

//  A DeclarativeAbstractRenderNode that Python can take functions over in. Every DeclarativeAbstractRenderNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteDeclarativeAbstractRenderNodeCall0)(const void *, const QSize *, int *);
typedef const QSize * (*CuteDeclarativeAbstractRenderNodeCall1)(const void *, int *);
typedef void (*CuteDeclarativeAbstractRenderNodeCall2)(const void *, const QRectF *, int *);
typedef void (*CuteDeclarativeAbstractRenderNodeCall3)(const void *, bool, int *);
typedef bool (*CuteDeclarativeAbstractRenderNodeCall4)(const void *, int *);
typedef void (*CuteDeclarativeAbstractRenderNodeCall5)(const void *, int *);
class CuteDeclarativeAbstractRenderNode : public DeclarativeAbstractRenderNode {
public:
  using DeclarativeAbstractRenderNode::DeclarativeAbstractRenderNode;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN29DeclarativeAbstractRenderNode14setTextureSizeERK5QSize")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK29DeclarativeAbstractRenderNode11textureSizeEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29DeclarativeAbstractRenderNode7setRectERK6QRectF")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN29DeclarativeAbstractRenderNode15setAntialiasingEb")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[5] = call;
      return true;
    }
    return false;
  }

  //  void DeclarativeAbstractRenderNode::setTextureSize(const QSize
  //      &textureSize)
  void setTextureSize(const QSize &textureSize) override {
    if (taken[0]) {
      int handled = 0;
      CuteDeclarativeAbstractRenderNodeCall0 call = reinterpret_cast<CuteDeclarativeAbstractRenderNodeCall0>(taken[0]);
      call(this, &textureSize, &handled);
      if (handled) return;
    }
  }

  //  QSize DeclarativeAbstractRenderNode::textureSize() const
  QSize textureSize() const override {
    if (taken[1]) {
      int handled = 0;
      CuteDeclarativeAbstractRenderNodeCall1 call = reinterpret_cast<CuteDeclarativeAbstractRenderNodeCall1>(taken[1]);
      const QSize * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void DeclarativeAbstractRenderNode::setRect(const QRectF &rect)
  void setRect(const QRectF &rect) override {
    if (taken[2]) {
      int handled = 0;
      CuteDeclarativeAbstractRenderNodeCall2 call = reinterpret_cast<CuteDeclarativeAbstractRenderNodeCall2>(taken[2]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  void DeclarativeAbstractRenderNode::setAntialiasing(bool enable)
  void setAntialiasing(bool enable) override {
    if (taken[3]) {
      int handled = 0;
      CuteDeclarativeAbstractRenderNodeCall3 call = reinterpret_cast<CuteDeclarativeAbstractRenderNodeCall3>(taken[3]);
      call(this, enable, &handled);
      if (handled) return;
    }
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[4]) {
      int handled = 0;
      CuteDeclarativeAbstractRenderNodeCall4 call = reinterpret_cast<CuteDeclarativeAbstractRenderNodeCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[5]) {
      int handled = 0;
      CuteDeclarativeAbstractRenderNodeCall5 call = reinterpret_cast<CuteDeclarativeAbstractRenderNodeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  void DeclarativeAbstractRenderNode::setTextureSize(const QSize
//      &textureSize)
extern "C" Q_DECL_EXPORT
void ritual_ZN29DeclarativeAbstractRenderNode14setTextureSizeERK5QSize(
    DeclarativeAbstractRenderNode *self,
    const QSize *textureSize) {
  self->setTextureSize(*textureSize);
}

//  QSize DeclarativeAbstractRenderNode::textureSize() const
extern "C" Q_DECL_EXPORT
QSize *ritual_ZNK29DeclarativeAbstractRenderNode11textureSizeEv(
    const DeclarativeAbstractRenderNode *self) {
  return new QSize(self->textureSize());
}

//  void DeclarativeAbstractRenderNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN29DeclarativeAbstractRenderNode7setRectERK6QRectF(
    DeclarativeAbstractRenderNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void DeclarativeAbstractRenderNode::setSeriesData(bool mapDirty, const
//      GLXYDataMap &dataMap)
extern "C" Q_DECL_EXPORT
void ritual_ZN29DeclarativeAbstractRenderNode13setSeriesDataEbRK5QHashIPK9QXYSeriesP14GLXYSeriesDataE(
    DeclarativeAbstractRenderNode *self,
    bool mapDirty,
    const GLXYDataMap *dataMap) {
  self->setSeriesData(mapDirty, *dataMap);
}

//  void DeclarativeAbstractRenderNode::setAntialiasing(bool enable)
extern "C" Q_DECL_EXPORT
void ritual_ZN29DeclarativeAbstractRenderNode15setAntialiasingEb(
    DeclarativeAbstractRenderNode *self,
    bool enable) {
  self->setAntialiasing(enable);
}

//  void DeclarativeAbstractRenderNode::addMouseEvents(const
//      QList<QMouseEvent *> &events)
extern "C" Q_DECL_EXPORT
void ritual_ZN29DeclarativeAbstractRenderNode14addMouseEventsERK5QListIP11QMouseEventE(
    DeclarativeAbstractRenderNode *self,
    const QList<QMouseEvent *> *events) {
  self->addMouseEvents(*events);
}

//  void DeclarativeAbstractRenderNode::takeMouseEventResponses(QList<MouseEv
//      entResponse> &responses)
extern "C" Q_DECL_EXPORT
void ritual_ZN29DeclarativeAbstractRenderNode23takeMouseEventResponsesER5QListI18MouseEventResponseE(
    DeclarativeAbstractRenderNode *self,
    QList<MouseEventResponse> *responses) {
  self->takeMouseEventResponses(*responses);
}

//  a Python function taken by a CuteDeclarativeAbstractRenderNode, for the
//      function named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_DeclarativeAbstractRenderNode(
    DeclarativeAbstractRenderNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteDeclarativeAbstractRenderNode *>(self)->take(key, call);
}
