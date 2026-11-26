//  Written by dev_tooling.RitualGenerator from the records of
//  QtCanvasPainter/qcanvascustombrush.h, Qt 6.12.0. Changes made here are
//  lost.
#include <QtCore/6.12.0/QtCore/private/qglobal_p.h>
#include <QtCanvasPainter/qcanvascustombrush.h>
#include <QtCanvasPainter/qcanvasbrush.h>
#include <QtCore/qvariant.h>
#include <QtCore/qstring.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/rhi/qshader.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qvectornd.h>
#include <QtCore/qdebug.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCanvasPainter/qcanvascustombrush.h>
#include <QtCanvasPainter/private/qcanvascustombrush_p.h>
#include <QtCore/QFile>
#include <QtCore/QDebug>
#include <QtCore/QDataStream>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from ../qtcanvaspainter/src/canvaspainter/qcanvascustombrush.cpp, line 538, as _ZN25QCanvasCustomBrushPrivate5cloneEv
inline QCanvasBrushPrivate *QCanvasCustomBrushPrivate::clone()
{
    return new QCanvasCustomBrushPrivate(*this);
}

//  from ../qtcanvaspainter/src/canvaspainter/qcanvascustombrush.cpp, line 328, as _ZNK25QCanvasCustomBrushPrivate6equalsERK19QCanvasBrushPrivate
inline bool QCanvasCustomBrushPrivate::equals(const QCanvasBrushPrivate &other) const noexcept
{
    Q_ASSERT(other.type == type);
    const auto &bd = static_cast<const QCanvasCustomBrushPrivate &>(other);

    if (fragmentShader != bd.fragmentShader
        || vertexShader != bd.vertexShader
        || timeRunning != bd.timeRunning
        || time != bd.time
        || data[0] != bd.data[0]
        || data[1] != bd.data[1]
        || data[2] != bd.data[2]
        || data[3] != bd.data[3])
        return false;

    return true;
}
//  -----------------------------------------------------------------------

//  QCanvasCustomBrush::QCanvasCustomBrush()
extern "C" Q_DECL_EXPORT
QCanvasCustomBrush *ritual_ZN18QCanvasCustomBrushC1Ev() {
  return new QCanvasCustomBrush();
}

//  QCanvasCustomBrush::QCanvasCustomBrush(const QCanvasCustomBrush &a0)
extern "C" Q_DECL_EXPORT
QCanvasCustomBrush *ritual_ZN18QCanvasCustomBrushC1ERKS_(
    const QCanvasCustomBrush *a0) {
  return new QCanvasCustomBrush(*a0);
}

//  QCanvasCustomBrush &QCanvasCustomBrush::operator=(const
//      QCanvasCustomBrush &a0)
extern "C" Q_DECL_EXPORT
QCanvasCustomBrush *ritual_ZN18QCanvasCustomBrushaSERKS_(
    QCanvasCustomBrush *self,
    const QCanvasCustomBrush *a0) {
  return &(self->operator=(*a0));
}

//  QCanvasCustomBrush::QCanvasCustomBrush(QCanvasCustomBrush &&a0)
extern "C" Q_DECL_EXPORT
QCanvasCustomBrush *ritual_ZN18QCanvasCustomBrushC1EOS_(
    QCanvasCustomBrush *a0) {
  return new QCanvasCustomBrush(std::move(*a0));
}

//  QCanvasCustomBrush &QCanvasCustomBrush::operator=(QCanvasCustomBrush
//      &&other)
extern "C" Q_DECL_EXPORT
QCanvasCustomBrush *ritual_ZN18QCanvasCustomBrushaSEOS_(
    QCanvasCustomBrush *self,
    QCanvasCustomBrush *other) {
  return &(self->operator=(std::move(*other)));
}

//  QCanvasCustomBrush::~QCanvasCustomBrush()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrushD1Ev(QCanvasCustomBrush *self) {
  delete self;
}

//  QCanvasBrush QCanvasCustomBrush::operator QCanvasBrush() const
extern "C" Q_DECL_EXPORT
QCanvasBrush *ritual_ZNK18QCanvasCustomBrushcv12QCanvasBrushEv(
    const QCanvasCustomBrush *self) {
  return new QCanvasBrush(self->operator QCanvasBrush());
}

//  QVariant QCanvasCustomBrush::operator QVariant() const
extern "C" Q_DECL_EXPORT
QVariant *ritual_ZNK18QCanvasCustomBrushcv8QVariantEv(
    const QCanvasCustomBrush *self) {
  return new QVariant(self->operator QVariant());
}

//  void QCanvasCustomBrush::setFragmentShader(const QString &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush17setFragmentShaderERK7QString(
    QCanvasCustomBrush *self,
    const QString *fragmentShader) {
  self->setFragmentShader(*fragmentShader);
}

//  void QCanvasCustomBrush::setFragmentShader(const QShader &fragmentShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush17setFragmentShaderERK7QShader(
    QCanvasCustomBrush *self,
    const QShader *fragmentShader) {
  self->setFragmentShader(*fragmentShader);
}

//  void QCanvasCustomBrush::setVertexShader(const QString &vertexShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush15setVertexShaderERK7QString(
    QCanvasCustomBrush *self,
    const QString *vertexShader) {
  self->setVertexShader(*vertexShader);
}

//  void QCanvasCustomBrush::setVertexShader(const QShader &vertexShader)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush15setVertexShaderERK7QShader(
    QCanvasCustomBrush *self,
    const QShader *vertexShader) {
  self->setVertexShader(*vertexShader);
}

//  bool QCanvasCustomBrush::isAnimationRunning() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK18QCanvasCustomBrush18isAnimationRunningEv(
    const QCanvasCustomBrush *self) {
  return self->isAnimationRunning();
}

//  void QCanvasCustomBrush::setAnimationRunning(bool running)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush19setAnimationRunningEb(
    QCanvasCustomBrush *self,
    bool running) {
  self->setAnimationRunning(running);
}

//  void QCanvasCustomBrush::setData1(const QVector4D &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush8setData1ERK9QVector4D(
    QCanvasCustomBrush *self,
    const QVector4D *data) {
  self->setData1(*data);
}

//  void QCanvasCustomBrush::setData2(const QVector4D &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush8setData2ERK9QVector4D(
    QCanvasCustomBrush *self,
    const QVector4D *data) {
  self->setData2(*data);
}

//  void QCanvasCustomBrush::setData3(const QVector4D &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush8setData3ERK9QVector4D(
    QCanvasCustomBrush *self,
    const QVector4D *data) {
  self->setData3(*data);
}

//  void QCanvasCustomBrush::setData4(const QVector4D &data)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush8setData4ERK9QVector4D(
    QCanvasCustomBrush *self,
    const QVector4D *data) {
  self->setData4(*data);
}

//  void QCanvasCustomBrush::swap(QCanvasCustomBrush &other)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QCanvasCustomBrush4swapERS_(
    QCanvasCustomBrush *self,
    QCanvasCustomBrush *other) {
  self->swap(*other);
}

//  bool operator==(const QCanvasCustomBrush &lhs, const QCanvasCustomBrush
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZeqRK18QCanvasCustomBrushS1_(
    const QCanvasCustomBrush *lhs,
    const QCanvasCustomBrush *rhs) {
  return operator==(*lhs, *rhs);
}

//  bool operator!=(const QCanvasCustomBrush &lhs, const QCanvasCustomBrush
//      &rhs)
extern "C" Q_DECL_EXPORT
bool ritual_ZneRK18QCanvasCustomBrushS1_(
    const QCanvasCustomBrush *lhs,
    const QCanvasCustomBrush *rhs) {
  return operator!=(*lhs, *rhs);
}

//  QCanvasCustomBrush::QCanvasCustomBrush(QCanvasCustomBrushPrivate *p)
extern "C" Q_DECL_EXPORT
QCanvasCustomBrush *ritual_ZN18QCanvasCustomBrushC1EP25QCanvasCustomBrushPrivate(
    QCanvasCustomBrushPrivate *p) {
  return new QCanvasCustomBrush(p);
}

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator<<(QDataStream &a0, const QCanvasCustomBrush &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZlsR11QDataStreamRK18QCanvasCustomBrush(
    QDataStream *a0,
    const QCanvasCustomBrush *a1) {
  return &(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DATASTREAM)
//  QDataStream &operator>>(QDataStream &a0, QCanvasCustomBrush &a1)
extern "C" Q_DECL_EXPORT
QDataStream *ritual_ZrsR11QDataStreamR18QCanvasCustomBrush(
    QDataStream *a0,
    QCanvasCustomBrush *a1) {
  return &(operator>>(*a0, *a1));
}
#endif  // !defined(QT_NO_DATASTREAM)

#if !defined(QT_NO_DEBUG_STREAM)
//  QDebug operator<<(QDebug a0, const QCanvasCustomBrush &a1)
extern "C" Q_DECL_EXPORT
QDebug *ritual_Zls6QDebugRK18QCanvasCustomBrush(
    const QDebug *a0,
    const QCanvasCustomBrush *a1) {
  return new QDebug(operator<<(*a0, *a1));
}
#endif  // !defined(QT_NO_DEBUG_STREAM)
