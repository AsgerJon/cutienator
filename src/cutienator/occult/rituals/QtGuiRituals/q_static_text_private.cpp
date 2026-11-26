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
#include <QtGui/qstatictext.h>
#include <QtGui/private/qstatictext_p.h>
#include <QtCore/qmath.h>
#include <QtGui/private/qtextengine_p.h>
#include <QtGui/private/qfontengine_p.h>
#include <QtGui/qabstracttextdocumentlayout.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER

//  Qt's own code, from here to the line of dashes: taken from
//  Qt's source, because Qt's library carries it under no name.
//  Copyright (C) The Qt Company Ltd. It is licensed
//  LGPL-3.0-only OR GPL-2.0-only OR GPL-3.0-only, and stays so
//  here. Each function is as Qt wrote it, with the word
//  'inline' put before it where Qt did not write it.

//  from src/gui/text/qstatictext.cpp, line 398, as local:qstatictext.cpp:DrawTextItemRecorder
namespace {
class DrawTextItemRecorder: public QPaintEngine
    {
    public:
        DrawTextItemRecorder(bool untransformedCoordinates, bool useBackendOptimizations)
                : m_dirtyPen(false), m_useBackendOptimizations(useBackendOptimizations),
                  m_untransformedCoordinates(untransformedCoordinates), m_currentColor(0, 0, 0, 0)
        {
        }

        virtual void updateState(const QPaintEngineState &newState) override
        {
            if (newState.state() & QPaintEngine::DirtyPen
                && newState.pen().color() != m_currentColor) {
                m_dirtyPen = true;
                m_currentColor = newState.pen().color();
            }
        }

        virtual void drawTextItem(const QPointF &position, const QTextItem &textItem) override
        {
            const QTextItemInt &ti = static_cast<const QTextItemInt &>(textItem);

            QStaticTextItem currentItem;
            currentItem.setFontEngine(ti.fontEngine);
            currentItem.font = ti.font();
            currentItem.glyphOffset = m_glyphs.size(); // Store offset into glyph pool
            currentItem.positionOffset = m_glyphs.size(); // Offset into position pool
            currentItem.useBackendOptimizations = m_useBackendOptimizations;
            if (m_dirtyPen)
                currentItem.color = m_currentColor;

            QTransform matrix = m_untransformedCoordinates ? QTransform() : state->transform();
            matrix.translate(position.x(), position.y());

            QVarLengthArray<glyph_t> glyphs;
            QVarLengthArray<QFixedPoint> positions;
            ti.fontEngine->getGlyphPositions(ti.glyphs, matrix, ti.flags, glyphs, positions);

            int size = glyphs.size();
            Q_ASSERT(size == positions.size());
            currentItem.numGlyphs = size;

            m_glyphs.resize(m_glyphs.size() + size);
            m_positions.resize(m_glyphs.size());

            glyph_t *glyphsDestination = m_glyphs.data() + currentItem.glyphOffset;
            memcpy(glyphsDestination, glyphs.constData(), sizeof(glyph_t) * currentItem.numGlyphs);

            QFixedPoint *positionsDestination = m_positions.data() + currentItem.positionOffset;
            memcpy(positionsDestination, positions.constData(), sizeof(QFixedPoint) * currentItem.numGlyphs);

            m_items.append(currentItem);
        }

        virtual void drawPolygon(const QPointF *, int , PolygonDrawMode ) override
        {
            /* intentionally empty */
        }

        virtual bool begin(QPaintDevice *) override  { return true; }
        virtual bool end() override { return true; }
        virtual void drawPixmap(const QRectF &, const QPixmap &, const QRectF &) override {}
        virtual Type type() const override
        {
            return User;
        }

        QList<QStaticTextItem> items() const
        {
            return m_items;
        }

        QList<QFixedPoint> positions() const
        {
            return m_positions;
        }

        QList<glyph_t> glyphs() const
        {
            return m_glyphs;
        }

    private:
        QList<QStaticTextItem> m_items;
        QList<QFixedPoint> m_positions;
        QList<glyph_t> m_glyphs;

        bool m_dirtyPen;
        bool m_useBackendOptimizations;
        bool m_untransformedCoordinates;
        QColor m_currentColor;
    };
}  // namespace

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
