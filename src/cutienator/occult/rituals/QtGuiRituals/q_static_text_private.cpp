//  Written by dev_tooling.RitualGenerator from the records of
//  QtGui/6.12.0/QtGui/private/qstatictext_p.h, Qt 6.12.0. Changes made here
//  are lost.
#include <QtGui/6.12.0/QtGui/private/qtguiglobal_p.h>
#include <QtGui/QtGui>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtGui/6.12.0/QtGui/private/qstatictext_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qpoint.h>
#include <QtGui/qcolor.h>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include "qstatictext.h"
#include "qstatictext_p.h"
#include <qmath.h>
#include <private/qtextengine_p.h>
#include <private/qfontengine_p.h>
#include <qabstracttextdocumentlayout.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qstatictext.cpp, line 369, as _ZN18QStaticTextPrivateC1Ev
inline QStaticTextPrivate::QStaticTextPrivate()
        : textWidth(-1.0), items(nullptr), itemCount(0), glyphPool(nullptr), positionPool(nullptr),
          needsRelayout(true), useBackendOptimizations(false), textFormat(Qt::AutoText),
          untransformedCoordinates(false)
{
}

//  from src/gui/text/qstatictext.cpp, line 376, as _ZN18QStaticTextPrivateC1ERKS_
inline QStaticTextPrivate::QStaticTextPrivate(const QStaticTextPrivate &other)
    : text(other.text), font(other.font), textWidth(other.textWidth), matrix(other.matrix),
      items(nullptr), itemCount(0), glyphPool(nullptr), positionPool(nullptr), textOption(other.textOption),
      needsRelayout(true), useBackendOptimizations(other.useBackendOptimizations),
      textFormat(other.textFormat), untransformedCoordinates(other.untransformedCoordinates)
{
}

//  from src/gui/text/qstatictext.cpp, line 384, as _ZN18QStaticTextPrivateD1Ev
inline QStaticTextPrivate::~QStaticTextPrivate()
{
    delete[] items;
    delete[] glyphPool;
    delete[] positionPool;
}

//  from src/gui/text/qstatictext.cpp, line 567, as _ZN18QStaticTextPrivate9paintTextERK7QPointFP8QPainterRK6QColor
inline void QStaticTextPrivate::paintText(const QPointF &topLeftPosition, QPainter *p, const QColor &pen)
{
    bool preferRichText = textFormat == Qt::RichText
                          || (textFormat == Qt::AutoText && Qt::mightBeRichText(text));

    if (!preferRichText) {
        QTextLayout textLayout;
        textLayout.setText(text);
        textLayout.setFont(font);
        textLayout.setTextOption(textOption);
        textLayout.setCacheEnabled(true);

        qreal height = 0;
        textLayout.beginLayout();
        while (1) {
            QTextLine line = textLayout.createLine();
            if (!line.isValid())
                break;
            line.setLeadingIncluded(true);

            if (textWidth >= 0.0)
                line.setLineWidth(textWidth);
            else
                line.setLineWidth(QFIXED_MAX);
            line.setPosition(QPointF(0.0, height));
            height += line.height();
            if (line.leading() < 0)
                height += qCeil(line.leading());
        }
        textLayout.endLayout();

        actualSize = textLayout.boundingRect().size();
        p->setPen(pen);
        textLayout.draw(p, topLeftPosition);
    } else {
        QTextDocument document;
#ifndef QT_NO_CSSPARSER
        document.setDefaultStyleSheet(QString::fromLatin1("body { color: rgba(%1, %2, %3, %4%) }")
                                      .arg(QString::number(pen.red()))
                                      .arg(QString::number(pen.green()))
                                      .arg(QString::number(pen.blue()))
                                      .arg(QString::number(pen.alpha())));
#endif
        document.setDefaultFont(font);
        document.setDocumentMargin(0.0);
#ifndef QT_NO_TEXTHTMLPARSER
        document.setHtml(text);
#else
        document.setPlainText(text);
#endif
        if (textWidth >= 0.0)
            document.setTextWidth(textWidth);
        else
            document.adjustSize();
        document.setDefaultTextOption(textOption);

        p->save();
        p->translate(topLeftPosition);
        QAbstractTextDocumentLayout::PaintContext ctx;
        ctx.palette.setColor(QPalette::Text, pen);
        document.documentLayout()->draw(p, ctx);
        p->restore();

        actualSize = document.size();
    }
}

//  from src/gui/text/qstatictext.cpp, line 391, as _ZN18QStaticTextPrivate3getEPK11QStaticText
inline QStaticTextPrivate *QStaticTextPrivate::get(const QStaticText *q)
{
    return q->data.data();
}
//  -----------------------------------------------------------------------

//  QStaticTextPrivate::QStaticTextPrivate()
extern "C" Q_DECL_EXPORT
QStaticTextPrivate *ritual_ZN18QStaticTextPrivateC1Ev() {
  return new QStaticTextPrivate();
}

//  QStaticTextPrivate::QStaticTextPrivate(const QStaticTextPrivate &other)
extern "C" Q_DECL_EXPORT
QStaticTextPrivate *ritual_ZN18QStaticTextPrivateC1ERKS_(
    const QStaticTextPrivate *other) {
  return new QStaticTextPrivate(*other);
}

//  QStaticTextPrivate::~QStaticTextPrivate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStaticTextPrivateD1Ev(QStaticTextPrivate *self) {
  delete self;
}

//  void QStaticTextPrivate::paintText(const QPointF &pos, QPainter *p, const
//      QColor &pen)
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStaticTextPrivate9paintTextERK7QPointFP8QPainterRK6QColor(
    QStaticTextPrivate *self,
    const QPointF *pos,
    QPainter *p,
    const QColor *pen) {
  self->paintText(*pos, p, *pen);
}

//  void QStaticTextPrivate::invalidate()
extern "C" Q_DECL_EXPORT
void ritual_ZN18QStaticTextPrivate10invalidateEv(QStaticTextPrivate *self) {
  self->invalidate();
}

//  QStaticTextPrivate *QStaticTextPrivate::get(const QStaticText *q)
extern "C" Q_DECL_EXPORT
QStaticTextPrivate *ritual_ZN18QStaticTextPrivate3getEPK11QStaticText(
    const QStaticText *q) {
  return QStaticTextPrivate::get(q);
}
