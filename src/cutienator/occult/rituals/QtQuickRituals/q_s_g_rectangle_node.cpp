//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/qsgrectanglenode.h, Qt 6.12.0. Changes made here are lost.
#include <QtQuick/QtQuick>
#include <QtQuick/qsgrectanglenode.h>
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <cstring>

//  A QSGRectangleNode that Python can take functions over in. Every QSGRectangleNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGRectangleNodeCall0)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGRectangleNodeCall1)(const void *, int *);
typedef void (*CuteQSGRectangleNodeCall2)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGRectangleNodeCall3)(const void *, int *);
typedef bool (*CuteQSGRectangleNodeCall4)(const void *, int *);
typedef void (*CuteQSGRectangleNodeCall5)(const void *, int *);
class CuteQSGRectangleNode : public QSGRectangleNode {
public:
  using QSGRectangleNode::QSGRectangleNode;
  void *taken[6] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN16QSGRectangleNode7setRectERK6QRectF")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRectangleNode4rectEv")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN16QSGRectangleNode8setColorERK6QColor")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK16QSGRectangleNode5colorEv")) {
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

  //  void QSGRectangleNode::setRect(const QRectF &rect)
  void setRect(const QRectF &rect) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRectangleNodeCall0 call = reinterpret_cast<CuteQSGRectangleNodeCall0>(taken[0]);
      call(this, &rect, &handled);
      if (handled) return;
    }
  }

  //  QRectF QSGRectangleNode::rect() const
  QRectF rect() const override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRectangleNodeCall1 call = reinterpret_cast<CuteQSGRectangleNodeCall1>(taken[1]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  void QSGRectangleNode::setColor(const QColor &color)
  void setColor(const QColor &color) override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRectangleNodeCall2 call = reinterpret_cast<CuteQSGRectangleNodeCall2>(taken[2]);
      call(this, &color, &handled);
      if (handled) return;
    }
  }

  //  QColor QSGRectangleNode::color() const
  QColor color() const override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRectangleNodeCall3 call = reinterpret_cast<CuteQSGRectangleNodeCall3>(taken[3]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return {};
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRectangleNodeCall4 call = reinterpret_cast<CuteQSGRectangleNodeCall4>(taken[4]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRectangleNodeCall5 call = reinterpret_cast<CuteQSGRectangleNodeCall5>(taken[5]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  QSGRectangleNode::~QSGRectangleNode()
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRectangleNodeD1Ev(QSGRectangleNode *self) {
  delete self;
}

//  void QSGRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRectangleNode7setRectERK6QRectF(
    QSGRectangleNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  void QSGRectangleNode::setRect(qreal x, qreal y, qreal w, qreal h)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRectangleNode7setRectEdddd(
    QSGRectangleNode *self,
    qreal x,
    qreal y,
    qreal w,
    qreal h) {
  self->setRect(x, y, w, h);
}

//  QRectF QSGRectangleNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK16QSGRectangleNode4rectEv(const QSGRectangleNode *self) {
  return new QRectF(self->rect());
}

//  void QSGRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN16QSGRectangleNode8setColorERK6QColor(
    QSGRectangleNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QSGRectangleNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK16QSGRectangleNode5colorEv(const QSGRectangleNode *self) {
  return new QColor(self->color());
}

//  a Python function taken by a CuteQSGRectangleNode, for the function named
//      by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRectangleNode(
    QSGRectangleNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRectangleNode *>(self)->take(key, call);
}
