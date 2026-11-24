//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgsoftwarepublicnodes_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgsoftwarepublicnodes_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/private/qsgsoftwarepublicnodes_p.h>
#include <QtQuick/private/qsgsoftwarelayer_p.h>
#include <QtQuick/private/qsgsoftwarepixmaptexture_p.h>
#include <QtQuick/private/qsgsoftwareinternalimagenode_p.h>
#include <QtQuick/private/qsgplaintexture_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 13, as _ZN24QSGSoftwareRectangleNodeC1Ev
inline QSGSoftwareRectangleNode::QSGSoftwareRectangleNode()
    : m_color(QColor(255, 255, 255))
{
    setMaterial((QSGMaterial*)1);
    setGeometry((QSGGeometry*)1);
}

//  from ../qtdeclarative/src/quick/scenegraph/adaptations/software/qsgsoftwarepublicnodes.cpp, line 20, as _ZN24QSGSoftwareRectangleNode5paintEP8QPainter
inline void QSGSoftwareRectangleNode::paint(QPainter *painter)
{
    painter->fillRect(m_rect, m_color);
}
//  -----------------------------------------------------------------------

//  QSGSoftwareRectangleNode::QSGSoftwareRectangleNode()
extern "C" Q_DECL_EXPORT
QSGSoftwareRectangleNode *ritual_ZN24QSGSoftwareRectangleNodeC1Ev() {
  return new QSGSoftwareRectangleNode();
}

//  void QSGSoftwareRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareRectangleNode7setRectERK6QRectF(
    QSGSoftwareRectangleNode *self,
    const QRectF *rect) {
  self->setRect(*rect);
}

//  QRectF QSGSoftwareRectangleNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_ZNK24QSGSoftwareRectangleNode4rectEv(
    const QSGSoftwareRectangleNode *self) {
  return new QRectF(self->rect());
}

//  void QSGSoftwareRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareRectangleNode8setColorERK6QColor(
    QSGSoftwareRectangleNode *self,
    const QColor *color) {
  self->setColor(*color);
}

//  QColor QSGSoftwareRectangleNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK24QSGSoftwareRectangleNode5colorEv(
    const QSGSoftwareRectangleNode *self) {
  return new QColor(self->color());
}

//  void QSGSoftwareRectangleNode::paint(QPainter *painter)
extern "C" Q_DECL_EXPORT
void ritual_ZN24QSGSoftwareRectangleNode5paintEP8QPainter(
    QSGSoftwareRectangleNode *self,
    QPainter *painter) {
  self->paint(painter);
}

//  void QSGSoftwareRectangleNode::setRect(const QRectF &rect)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGSoftwareRectangleNode7setRectERK6QRectF(
    QSGSoftwareRectangleNode *self,
    const QRectF *rect) {
  self->QSGSoftwareRectangleNode::setRect(*rect);
}

//  QRectF QSGSoftwareRectangleNode::rect() const
extern "C" Q_DECL_EXPORT
QRectF *ritual_own_ZNK24QSGSoftwareRectangleNode4rectEv(
    const QSGSoftwareRectangleNode *self) {
  return new QRectF(self->QSGSoftwareRectangleNode::rect());
}

//  void QSGSoftwareRectangleNode::setColor(const QColor &color)
extern "C" Q_DECL_EXPORT
void ritual_own_ZN24QSGSoftwareRectangleNode8setColorERK6QColor(
    QSGSoftwareRectangleNode *self,
    const QColor *color) {
  self->QSGSoftwareRectangleNode::setColor(*color);
}

//  QColor QSGSoftwareRectangleNode::color() const
extern "C" Q_DECL_EXPORT
QColor *ritual_own_ZNK24QSGSoftwareRectangleNode5colorEv(
    const QSGSoftwareRectangleNode *self) {
  return new QColor(self->QSGSoftwareRectangleNode::color());
}
