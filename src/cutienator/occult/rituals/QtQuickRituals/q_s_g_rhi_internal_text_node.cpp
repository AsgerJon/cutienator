//  Written by dev_tooling.RitualGenerator from the records of
//  QtQuick/6.12.0/QtQuick/private/qsgrhiinternaltextnode_p.h, Qt 6.12.0.
//  Changes made here are lost.
#include <QtQuick/6.12.0/QtQuick/private/qtquickglobal_p.h>
#include <QtQuick/QtQuick>
#ifndef CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtQuick/6.12.0/QtQuick/private/qsgrhiinternaltextnode_p.h>
#endif  // CUTIENATOR_NOT_IN_COMMON_HEADER
#include <QtCore/qrect.h>
#include <QtGui/qcolor.h>
#include <QtCore/qpoint.h>
#include <cstring>

//  A QSGRhiInternalTextNode that Python can take functions over in. Every QSGRhiInternalTextNode
//  Python makes is one. Each function below asks the Python
//  function handed over for it, and runs Qt's own without one.
typedef void (*CuteQSGRhiInternalTextNodeCall0)(const void *, const QRectF *, const QColor *, int, QSGInternalTextNode::RecycleBin *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall1)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGRhiInternalTextNodeCall2)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall3)(const void *, int, int *);
typedef int (*CuteQSGRhiInternalTextNodeCall4)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall5)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGRhiInternalTextNodeCall6)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall7)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGRhiInternalTextNodeCall8)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall9)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGRhiInternalTextNodeCall10)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall11)(const void *, const QColor *, int *);
typedef const QColor * (*CuteQSGRhiInternalTextNodeCall12)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall13)(const void *, int, int *);
typedef int (*CuteQSGRhiInternalTextNodeCall14)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall15)(const void *, int, int *);
typedef int (*CuteQSGRhiInternalTextNodeCall16)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall17)(const void *, int, int *);
typedef int (*CuteQSGRhiInternalTextNodeCall18)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall19)(const void *, const QRectF *, int *);
typedef const QRectF * (*CuteQSGRhiInternalTextNodeCall20)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall21)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall22)(const void *, const QPointF *, QTextLayout *, int, int, int, int, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall23)(const void *, const QPointF *, QTextDocument *, int, int, int *);
typedef bool (*CuteQSGRhiInternalTextNodeCall24)(const void *, int *);
typedef void (*CuteQSGRhiInternalTextNodeCall25)(const void *, int *);
class CuteQSGRhiInternalTextNode : public QSGRhiInternalTextNode {
public:
  using QSGRhiInternalTextNode::QSGRhiInternalTextNode;
  void *taken[26] = {};

  bool take(const char *key, void *call) {
    if (!std::strcmp(key, "_ZN19QSGInternalTextNode17addDecorationNodeERK6QRectFRK6QColorN15QTextCharFormat14UnderlineStyleEPNS_10RecycleBinE")) {
      taken[0] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode8setColorE6QColor")) {
      taken[1] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode5colorEv")) {
      taken[2] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode12setTextStyleENS_9TextStyleE")) {
      taken[3] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode9textStyleEv")) {
      taken[4] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode13setStyleColorE6QColor")) {
      taken[5] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode10styleColorEv")) {
      taken[6] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode12setLinkColorE6QColor")) {
      taken[7] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode9linkColorEv")) {
      taken[8] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode17setSelectionColorE6QColor")) {
      taken[9] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode14selectionColorEv")) {
      taken[10] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode21setSelectionTextColorE6QColor")) {
      taken[11] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode18selectionTextColorEv")) {
      taken[12] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode20setRenderTypeQualityEi")) {
      taken[13] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode17renderTypeQualityEv")) {
      taken[14] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode13setRenderTypeENS_10RenderTypeE")) {
      taken[15] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode10renderTypeEv")) {
      taken[16] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode12setFilteringEN10QSGTexture9FilteringE")) {
      taken[17] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode9filteringEv")) {
      taken[18] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode11setViewportERK6QRectF")) {
      taken[19] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK11QSGTextNode8viewportEv")) {
      taken[20] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode5clearEv")) {
      taken[21] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode15doAddTextLayoutE7QPointFP11QTextLayoutiiii")) {
      taken[22] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN11QSGTextNode17doAddTextDocumentE7QPointFP13QTextDocumentii")) {
      taken[23] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZNK7QSGNode16isSubtreeBlockedEv")) {
      taken[24] = call;
      return true;
    }
    if (!std::strcmp(key, "_ZN7QSGNode10preprocessEv")) {
      taken[25] = call;
      return true;
    }
    return false;
  }

  //  void QSGRhiInternalTextNode::addDecorationNode(const QRectF &rect,
  //      const QColor &color, QTextCharFormat::UnderlineStyle style,
  //      RecycleBin *recycleBin)
  void addDecorationNode(
      const QRectF &rect,
      const QColor &color,
      QTextCharFormat::UnderlineStyle style,
      QSGInternalTextNode::RecycleBin *recycleBin) override {
    if (taken[0]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall0 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall0>(taken[0]);
      call(this, &rect, &color, static_cast<int>(style), recycleBin, &handled);
      if (handled) return;
    }
    QSGRhiInternalTextNode::addDecorationNode(rect, color, style, recycleBin);
  }

  //  void QSGInternalTextNode::setColor(QColor color)
  void setColor(QColor color) override {
    if (taken[1]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall1 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall1>(taken[1]);
      call(this, &color, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setColor(color);
  }

  //  QColor QSGInternalTextNode::color() const
  QColor color() const override {
    if (taken[2]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall2 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall2>(taken[2]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::color();
  }

  //  void QSGInternalTextNode::setTextStyle(TextStyle textStyle)
  void setTextStyle(QSGTextNode::TextStyle textStyle) override {
    if (taken[3]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall3 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall3>(taken[3]);
      call(this, static_cast<int>(textStyle), &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setTextStyle(textStyle);
  }

  //  TextStyle QSGInternalTextNode::textStyle()
  QSGTextNode::TextStyle textStyle() override {
    if (taken[4]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall4 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall4>(taken[4]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTextNode::TextStyle>(given);
    }
    return QSGInternalTextNode::textStyle();
  }

  //  void QSGInternalTextNode::setStyleColor(QColor styleColor)
  void setStyleColor(QColor styleColor) override {
    if (taken[5]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall5 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall5>(taken[5]);
      call(this, &styleColor, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setStyleColor(styleColor);
  }

  //  QColor QSGInternalTextNode::styleColor() const
  QColor styleColor() const override {
    if (taken[6]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall6 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall6>(taken[6]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::styleColor();
  }

  //  void QSGInternalTextNode::setLinkColor(QColor linkColor)
  void setLinkColor(QColor linkColor) override {
    if (taken[7]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall7 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall7>(taken[7]);
      call(this, &linkColor, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setLinkColor(linkColor);
  }

  //  QColor QSGInternalTextNode::linkColor() const
  QColor linkColor() const override {
    if (taken[8]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall8 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall8>(taken[8]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::linkColor();
  }

  //  void QSGInternalTextNode::setSelectionColor(QColor selectionColor)
  void setSelectionColor(QColor selectionColor) override {
    if (taken[9]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall9 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall9>(taken[9]);
      call(this, &selectionColor, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setSelectionColor(selectionColor);
  }

  //  QColor QSGInternalTextNode::selectionColor() const
  QColor selectionColor() const override {
    if (taken[10]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall10 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall10>(taken[10]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::selectionColor();
  }

  //  void QSGInternalTextNode::setSelectionTextColor(QColor
  //      selectionTextColor)
  void setSelectionTextColor(QColor selectionTextColor) override {
    if (taken[11]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall11 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall11>(taken[11]);
      call(this, &selectionTextColor, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setSelectionTextColor(selectionTextColor);
  }

  //  QColor QSGInternalTextNode::selectionTextColor() const
  QColor selectionTextColor() const override {
    if (taken[12]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall12 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall12>(taken[12]);
      const QColor * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::selectionTextColor();
  }

  //  void QSGInternalTextNode::setRenderTypeQuality(int renderTypeQuality)
  void setRenderTypeQuality(int renderTypeQuality) override {
    if (taken[13]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall13 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall13>(taken[13]);
      call(this, renderTypeQuality, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setRenderTypeQuality(renderTypeQuality);
  }

  //  int QSGInternalTextNode::renderTypeQuality() const
  int renderTypeQuality() const override {
    if (taken[14]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall14 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall14>(taken[14]);
      int given = call(this, &handled);
      if (handled) return given;
    }
    return QSGInternalTextNode::renderTypeQuality();
  }

  //  void QSGInternalTextNode::setRenderType(RenderType renderType)
  void setRenderType(QSGTextNode::RenderType renderType) override {
    if (taken[15]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall15 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall15>(taken[15]);
      call(this, static_cast<int>(renderType), &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setRenderType(renderType);
  }

  //  RenderType QSGInternalTextNode::renderType() const
  QSGTextNode::RenderType renderType() const override {
    if (taken[16]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall16 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall16>(taken[16]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTextNode::RenderType>(given);
    }
    return QSGInternalTextNode::renderType();
  }

  //  void QSGInternalTextNode::setFiltering(QSGTexture::Filtering
  //      filtering)
  void setFiltering(QSGTexture::Filtering filtering) override {
    if (taken[17]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall17 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall17>(taken[17]);
      call(this, static_cast<int>(filtering), &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setFiltering(filtering);
  }

  //  QSGTexture::Filtering QSGInternalTextNode::filtering() const
  QSGTexture::Filtering filtering() const override {
    if (taken[18]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall18 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall18>(taken[18]);
      int given = call(this, &handled);
      if (handled) return static_cast<QSGTexture::Filtering>(given);
    }
    return QSGInternalTextNode::filtering();
  }

  //  void QSGInternalTextNode::setViewport(const QRectF &viewport)
  void setViewport(const QRectF &viewport) override {
    if (taken[19]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall19 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall19>(taken[19]);
      call(this, &viewport, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::setViewport(viewport);
  }

  //  QRectF QSGInternalTextNode::viewport() const
  QRectF viewport() const override {
    if (taken[20]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall20 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall20>(taken[20]);
      const QRectF * given = call(this, &handled);
      if (handled && given) return *given;
    }
    return QSGInternalTextNode::viewport();
  }

  //  void QSGInternalTextNode::clear()
  void clear() override {
    if (taken[21]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall21 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall21>(taken[21]);
      call(this, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::clear();
  }

  //  void QSGInternalTextNode::doAddTextLayout(QPointF position,
  //      QTextLayout *textLayout, int selectionStart, int selectionEnd,
  //      int lineStart, int lineCount)
  void doAddTextLayout(
      QPointF position,
      QTextLayout *textLayout,
      int selectionStart,
      int selectionEnd,
      int lineStart,
      int lineCount) override {
    if (taken[22]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall22 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall22>(taken[22]);
      call(this, &position, textLayout, selectionStart, selectionEnd, lineStart, lineCount, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::doAddTextLayout(position, textLayout, selectionStart, selectionEnd, lineStart, lineCount);
  }

  //  void QSGInternalTextNode::doAddTextDocument(QPointF position,
  //      QTextDocument *textDocument, int selectionStart, int
  //      selectionEnd)
  void doAddTextDocument(
      QPointF position,
      QTextDocument *textDocument,
      int selectionStart,
      int selectionEnd) override {
    if (taken[23]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall23 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall23>(taken[23]);
      call(this, &position, textDocument, selectionStart, selectionEnd, &handled);
      if (handled) return;
    }
    QSGInternalTextNode::doAddTextDocument(position, textDocument, selectionStart, selectionEnd);
  }

  //  bool QSGNode::isSubtreeBlocked() const
  bool isSubtreeBlocked() const override {
    if (taken[24]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall24 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall24>(taken[24]);
      bool given = call(this, &handled);
      if (handled) return given;
    }
    return QSGNode::isSubtreeBlocked();
  }

  //  void QSGNode::preprocess()
  void preprocess() override {
    if (taken[25]) {
      int handled = 0;
      CuteQSGRhiInternalTextNodeCall25 call = reinterpret_cast<CuteQSGRhiInternalTextNodeCall25>(taken[25]);
      call(this, &handled);
      if (handled) return;
    }
    QSGNode::preprocess();
  }
};

//  void QSGRhiInternalTextNode::addDecorationNode(const QRectF &rect, const
//      QColor &color, QTextCharFormat::UnderlineStyle style, RecycleBin
//      *recycleBin)
extern "C" Q_DECL_EXPORT
void ritual_ZN22QSGRhiInternalTextNode17addDecorationNodeERK6QRectFRK6QColorN15QTextCharFormat14UnderlineStyleEPN19QSGInternalTextNode10RecycleBinE(
    QSGRhiInternalTextNode *self,
    const QRectF *rect,
    const QColor *color,
    QTextCharFormat::UnderlineStyle style,
    QSGInternalTextNode::RecycleBin *recycleBin) {
  self->addDecorationNode(*rect, *color, style, recycleBin);
}

//  a Python function taken by a CuteQSGRhiInternalTextNode, for the function
//      named by the key
extern "C" Q_DECL_EXPORT
bool ritual_take_QSGRhiInternalTextNode(
    QSGRhiInternalTextNode *self,
    const char *key,
    void *call) {
  return static_cast<CuteQSGRhiInternalTextNode *>(self)->take(key, call);
}
