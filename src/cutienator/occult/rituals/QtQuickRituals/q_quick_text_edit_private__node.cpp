//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qquicktextedit_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qquicktextedit_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qdebug.h>

//  QQuickTextEditPrivate::Node::Node(int startPos, QSGInternalTextNode
//      *node)
extern "C" Q_DECL_EXPORT
QQuickTextEditPrivate::Node *ritual_ZN21QQuickTextEditPrivate4NodeC1EiP19QSGInternalTextNode(
    int startPos,
    QSGInternalTextNode *node) {
  return new QQuickTextEditPrivate::Node(startPos, node);
}

//  QSGInternalTextNode *QQuickTextEditPrivate::Node::textNode() const
extern "C" Q_DECL_EXPORT
QSGInternalTextNode *ritual_ZNK21QQuickTextEditPrivate4Node8textNodeEv(
    const QQuickTextEditPrivate::Node *self) {
  return self->textNode();
}

//  void QQuickTextEditPrivate::Node::moveStartPos(int delta)
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate4Node12moveStartPosEi(
    QQuickTextEditPrivate::Node *self,
    int delta) {
  self->moveStartPos(delta);
}

//  int QQuickTextEditPrivate::Node::startPos() const
extern "C" Q_DECL_EXPORT
int ritual_ZNK21QQuickTextEditPrivate4Node8startPosEv(
    const QQuickTextEditPrivate::Node *self) {
  return self->startPos();
}

//  void QQuickTextEditPrivate::Node::setDirty()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate4Node8setDirtyEv(
    QQuickTextEditPrivate::Node *self) {
  self->setDirty();
}

//  bool QQuickTextEditPrivate::Node::dirty() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK21QQuickTextEditPrivate4Node5dirtyEv(
    const QQuickTextEditPrivate::Node *self) {
  return self->dirty();
}

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const Node &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRKN21QQuickTextEditPrivate4NodeE(
    const QDebug *a0,
    const QQuickTextEditPrivate::Node *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)

//  QQuickTextEditPrivate::Node::~Node()
extern "C" Q_DECL_EXPORT
void ritual_ZN21QQuickTextEditPrivate4NodeD1Ev(
    QQuickTextEditPrivate::Node *self) {
  delete self;
}
