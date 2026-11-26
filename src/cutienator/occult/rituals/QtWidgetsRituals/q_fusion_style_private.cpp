//  Written by dev_tooling.RitualGenerator from the records of
//  QtWidgets/6.12.0/QtWidgets/private/qfusionstyle_p_p.h, Qt 6.12.0. Changes
//  made here are lost.
#include <QtWidgets/qtwidgetsglobal.h>
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(style_fusion)
#if QT_CONFIG(style_fusion)
#include <QtWidgets/6.12.0/QtWidgets/private/qtwidgetsglobal_p.h>
#if QT_CONFIG(style_fusion)
#include <QtWidgets/QtWidgets>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfusionstyle_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#endif
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/6.12.0/QtWidgets/private/qfusionstyle_p_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/qpalette.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtWidgets/private/qfusionstyle_p.h>
#include <QtWidgets/private/qfusionstyle_p_p.h>
#if QT_CONFIG(style_fusion) || defined(QT_PLUGIN)
#include <QtWidgets/private/qcommonstyle_p.h>
#if QT_CONFIG(combobox)
#include <QtWidgets/qcombobox.h>
#endif
#if QT_CONFIG(pushbutton)
#include <QtWidgets/qpushbutton.h>
#endif
#if QT_CONFIG(abstractbutton)
#include <QtWidgets/qabstractbutton.h>
#endif
#include <QtGui/qpainter.h>
#include <QtGui/qpainterpath.h>
#include <QtGui/qpainterstateguard.h>
#include <QtCore/qdir.h>
#include <QtWidgets/qstyleoption.h>
#include <QtWidgets/qapplication.h>
#if QT_CONFIG(mainwindow)
#include <QtWidgets/qmainwindow.h>
#endif
#include <QtGui/qfont.h>
#if QT_CONFIG(groupbox)
#include <QtWidgets/qgroupbox.h>
#endif
#include <QtGui/qpixmapcache.h>
#if QT_CONFIG(scrollbar)
#include <QtWidgets/qscrollbar.h>
#endif
#if QT_CONFIG(spinbox)
#include <QtWidgets/qspinbox.h>
#endif
#if QT_CONFIG(abstractslider)
#include <QtWidgets/qabstractslider.h>
#endif
#if QT_CONFIG(slider)
#include <QtWidgets/qslider.h>
#endif
#if QT_CONFIG(splitter)
#include <QtWidgets/qsplitter.h>
#endif
#if QT_CONFIG(progressbar)
#include <QtWidgets/qprogressbar.h>
#endif
#if QT_CONFIG(wizard)
#include <QtWidgets/qwizard.h>
#endif
#include <QtWidgets/qdrawutil.h>
#include <QtWidgets/private/qstylehelper_p.h>
#include <QtGui/private/qdrawhelper_p.h>
#include <QtWidgets/private/qapplication_p.h>
#include <QtWidgets/private/qwidget_p.h>
#include <QtGui/qstylehints.h>
#include <QtCore/qoperatingsystemversion.h>
#endif
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

using namespace Qt::StringLiterals;

//  from src/widgets/styles/qfusionstyle.cpp, line 250, as _ZN19QFusionStylePrivateC1Ev
#if QT_CONFIG(style_fusion) || defined(QT_PLUGIN)
inline QFusionStylePrivate::QFusionStylePrivate()
{
    animationFps = 60;
}
#endif  // QT_CONFIG(style_fusion) || defined(QT_PLUGIN)
//  -----------------------------------------------------------------------

//  QFusionStyle *QFusionStylePrivate::q_func()
extern "C" Q_DECL_EXPORT
QFusionStyle *ritual_ZN19QFusionStylePrivate6q_funcEv(
    QFusionStylePrivate *self) {
  return self->q_func();
}

//  const QFusionStyle *QFusionStylePrivate::q_func() const
extern "C" Q_DECL_EXPORT
const QFusionStyle *ritual_ZNK19QFusionStylePrivate6q_funcEv(
    const QFusionStylePrivate *self) {
  return self->q_func();
}

//  QFusionStylePrivate::QFusionStylePrivate()
extern "C" Q_DECL_EXPORT
QFusionStylePrivate *ritual_ZN19QFusionStylePrivateC1Ev() {
  return new QFusionStylePrivate();
}

//  bool QFusionStylePrivate::isMacSystemPalette(const QPalette &pal) const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFusionStylePrivate18isMacSystemPaletteERK8QPalette(
    const QFusionStylePrivate *self,
    const QPalette *pal) {
  return self->isMacSystemPalette(*pal);
}

//  QColor QFusionStylePrivate::highlight(const QPalette &pal) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QFusionStylePrivate9highlightERK8QPalette(
    const QFusionStylePrivate *self,
    const QPalette *pal) {
  return new QColor(self->highlight(*pal));
}

//  QColor QFusionStylePrivate::highlightedText(const QPalette &pal) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QFusionStylePrivate15highlightedTextERK8QPalette(
    const QFusionStylePrivate *self,
    const QPalette *pal) {
  return new QColor(self->highlightedText(*pal));
}

//  QColor QFusionStylePrivate::outline(const QPalette &pal) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QFusionStylePrivate7outlineERK8QPalette(
    const QFusionStylePrivate *self,
    const QPalette *pal) {
  return new QColor(self->outline(*pal));
}

//  QColor QFusionStylePrivate::highlightedOutline(const QPalette &pal) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QFusionStylePrivate18highlightedOutlineERK8QPalette(
    const QFusionStylePrivate *self,
    const QPalette *pal) {
  return new QColor(self->highlightedOutline(*pal));
}

//  QColor QFusionStylePrivate::tabFrameColor(const QPalette &pal) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QFusionStylePrivate13tabFrameColorERK8QPalette(
    const QFusionStylePrivate *self,
    const QPalette *pal) {
  return new QColor(self->tabFrameColor(*pal));
}

//  QColor QFusionStylePrivate::buttonColor(const QPalette &pal) const
extern "C" Q_DECL_EXPORT
QColor *ritual_ZNK19QFusionStylePrivate11buttonColorERK8QPalette(
    const QFusionStylePrivate *self,
    const QPalette *pal) {
  return new QColor(self->buttonColor(*pal));
}

//  Qt::ColorScheme QFusionStylePrivate::colorScheme() const
extern "C" Q_DECL_EXPORT
Qt::ColorScheme ritual_ZNK19QFusionStylePrivate11colorSchemeEv(
    const QFusionStylePrivate *self) {
  return self->colorScheme();
}

//  bool QFusionStylePrivate::isHighContrast() const
extern "C" Q_DECL_EXPORT
bool ritual_ZNK19QFusionStylePrivate14isHighContrastEv(
    const QFusionStylePrivate *self) {
  return self->isHighContrast();
}

#endif  // QT_CONFIG(style_fusion)
#endif  // QT_CONFIG(style_fusion)
