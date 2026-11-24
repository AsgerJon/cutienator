//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrenderer_p.h, Qt 6.12.0. Changes made
//  here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrenderer_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  void QSGNodeDumper::dump(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGNodeDumper4dumpEP7QSGNode(QSGNode *n) {
  QSGNodeDumper::dump(n);
}

//  QSGNodeDumper::QSGNodeDumper()
extern "C" Q_DECL_EXPORT
QSGNodeDumper *ritual_ZN13QSGNodeDumperC1Ev() {
  return new QSGNodeDumper();
}

//  void QSGNodeDumper::visitNode(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGNodeDumper9visitNodeEP7QSGNode(
    QSGNodeDumper *self,
    QSGNode *n) {
  self->visitNode(n);
}

//  void QSGNodeDumper::visitChildren(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGNodeDumper13visitChildrenEP7QSGNode(
    QSGNodeDumper *self,
    QSGNode *n) {
  self->visitChildren(n);
}

//  QSGNodeDumper::~QSGNodeDumper()
extern "C" Q_DECL_EXPORT
void ritual_ZN13QSGNodeDumperD1Ev(QSGNodeDumper *self) {
  delete self;
}

//  void QSGNodeDumper::visitNode(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSGNodeDumper9visitNodeEP7QSGNode(
    QSGNodeDumper *self,
    QSGNode *n) {
  self->QSGNodeDumper::visitNode(n);
}

//  void QSGNodeDumper::visitChildren(QSGNode *n)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN13QSGNodeDumper13visitChildrenEP7QSGNode(
    QSGNodeDumper *self,
    QSGNode *n) {
  self->QSGNodeDumper::visitChildren(n);
}
