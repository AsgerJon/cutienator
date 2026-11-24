//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/qtquickglobal.h>
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#if QT_CONFIG(quick_sprite)
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgadaptationlayer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtCore/qsize.h>
#include <cstring>

//  A QSGSpriteNode that Python can take functions over in. Every QSGSpriteNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall0)(const void *, QSGTexture *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall1)(const void *, float, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall2)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall3)(const void *, const QPoint *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall4)(const void *, const QSize *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall5)(const void *, const QSize *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall6)(const void *, const QSizeF *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall7)(const void *, int, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall8)(const void *, int *);
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
typedef void (*CuteQSGSpriteNodeCall9)(const void *, QSGNodeVisitorEx *, int *);
#endif  // QT_CONFIG(quick_sprite)
typedef bool (*CuteQSGSpriteNodeCall10)(const void *, int *);
typedef void (*CuteQSGSpriteNodeCall11)(const void *, int *);
class CuteQSGSpriteNode : public QSGSpriteNode {
public:
  using QSGSpriteNode::QSGSpriteNode;
  void *taken[12] = {};

  bool take(const char *key, void *call) {
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode10setTextureEP10QSGTexture")) {
      taken[0] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode7setTimeEf")) {
      taken[1] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode10setSourceAERK6QPoint")) {
      taken[2] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode10setSourceBERK6QPoint")) {
      taken[3] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode13setSpriteSizeERK5QSize")) {
      taken[4] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode12setSheetSizeERK5QSize")) {
      taken[5] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode7setSizeERK6QSizeF")) {
      taken[6] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode12setFilteringEN10QSGTexture9FilteringE")) {
      taken[7] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN13QSGSpriteNode6updateEv")) {
      taken[8] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
#if QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZN16QSGVisitableNode6acceptEP16QSGNodeVisitorEx")) {
      taken[9] = call;
      return true;
    }
#endif  // QT_CONFIG(quick_sprite)
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[11] = call;
      return true;
    }
    return false;
  }

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::setTexture(QSGTexture *texture)
  void setTexture(QSGTexture *texture) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGSpriteNodeCall0 call = reinterpret_cast<CuteQSGSpriteNodeCall0>(taken[0]);
      call(this, texture, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::setTime(float time)
  void setTime(float time) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGSpriteNodeCall1 call = reinterpret_cast<CuteQSGSpriteNodeCall1>(taken[1]);
      call(this, time, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::setSourceA(const QPoint &source)
  void setSourceA(const QPoint &source) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGSpriteNodeCall2 call = reinterpret_cast<CuteQSGSpriteNodeCall2>(taken[2]);
      call(this, &source, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::setSourceB(const QPoint &source)
  void setSourceB(const QPoint &source) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGSpriteNodeCall3 call = reinterpret_cast<CuteQSGSpriteNodeCall3>(taken[3]);
      call(this, &source, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::setSpriteSize(const QSize &size)
  void setSpriteSize(const QSize &size) override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGSpriteNodeCall4 call = reinterpret_cast<CuteQSGSpriteNodeCall4>(taken[4]);
      call(this, &size, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::setSheetSize(const QSize &size)
  void setSheetSize(const QSize &size) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGSpriteNodeCall5 call = reinterpret_cast<CuteQSGSpriteNodeCall5>(taken[5]);
      call(this, &size, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::setSize(const QSizeF &size)
  void setSize(const QSizeF &size) override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGSpriteNodeCall6 call = reinterpret_cast<CuteQSGSpriteNodeCall6>(taken[6]);
      call(this, &size, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::setFiltering(QSGTexture::Filtering filtering)
  void setFiltering(QSGTexture::Filtering filtering) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGSpriteNodeCall7 call = reinterpret_cast<CuteQSGSpriteNodeCall7>(taken[7]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::update()
  void update() override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGSpriteNodeCall8 call = reinterpret_cast<CuteQSGSpriteNodeCall8>(taken[8]);
      call(this, &handled);
      if (handled) return;
    }
  }
#endif  // QT_CONFIG(quick_sprite)

#if QT_CONFIG(quick_sprite)
  //  void QSGSpriteNode::accept(QSGNodeVisitorEx *visitor)
  void accept(QSGNodeVisitorEx *visitor) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGSpriteNodeCall9 call = reinterpret_cast<CuteQSGSpriteNodeCall9>(taken[9]);
      call(this, visitor, &handled);
      if (handled) return;
    }
    QSGSpriteNode::accept(visitor);
  }
#endif  // QT_CONFIG(quick_sprite)

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGSpriteNodeCall10 call = reinterpret_cast<CuteQSGSpriteNodeCall10>(taken[10]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGSpriteNodeCall11 call = reinterpret_cast<CuteQSGSpriteNodeCall11>(taken[11]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGSpriteNode::~QSGSpriteNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNodeD1Ev(QSGSpriteNode *self) {
  delete self;
}

//  void QSGSpriteNode::setTexture(QSGTexture *texture)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode10setTextureEP10QSGTexture(
    QSGSpriteNode *self,
    QSGTexture *texture) {
  self->setTexture(texture);
}

//  void QSGSpriteNode::setTime(float time)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode7setTimeEf(QSGSpriteNode *self, float time) {
  self->setTime(time);
}

//  void QSGSpriteNode::setSourceA(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode10setSourceAERK6QPoint(
    QSGSpriteNode *self,
    const QPoint *source) {
  self->setSourceA(*source);
}

//  void QSGSpriteNode::setSourceB(const QPoint &source)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode10setSourceBERK6QPoint(
    QSGSpriteNode *self,
    const QPoint *source) {
  self->setSourceB(*source);
}

//  void QSGSpriteNode::setSpriteSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode13setSpriteSizeERK5QSize(
    QSGSpriteNode *self,
    const QSize *size) {
  self->setSpriteSize(*size);
}

//  void QSGSpriteNode::setSheetSize(const QSize &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode12setSheetSizeERK5QSize(
    QSGSpriteNode *self,
    const QSize *size) {
  self->setSheetSize(*size);
}

//  void QSGSpriteNode::setSize(const QSizeF &size)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode7setSizeERK6QSizeF(
    QSGSpriteNode *self,
    const QSizeF *size) {
  self->setSize(*size);
}

//  void QSGSpriteNode::setFiltering(QSGTexture::Filtering filtering)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode12setFilteringEN10QSGTexture9FilteringE(
    QSGSpriteNode *self,
    QSGTexture::Filtering filtering) {
  self->setFiltering(filtering);
}

//  void QSGSpriteNode::update()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode6updateEv(QSGSpriteNode *self) {
  self->update();
}

//  void QSGSpriteNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGSpriteNode6acceptEP16QSGNodeVisitorEx(
    QSGSpriteNode *self,
    QSGNodeVisitorEx *visitor) {
  self->accept(visitor);
}

//  a Python function taken by a CuteQSGSpriteNode, for the function named by
//      the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGSpriteNode(
    QSGSpriteNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGSpriteNode *>(self)->take(key, call);
}

//  void QSGSpriteNode::accept(QSGNodeVisitorEx *visitor)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSGSpriteNode6acceptEP16QSGNodeVisitorEx(
    QSGSpriteNode *self,
    QSGNodeVisitorEx *visitor) {
  self->QSGSpriteNode::accept(visitor);
}

#endif  // QT_CONFIG(quick_sprite)
