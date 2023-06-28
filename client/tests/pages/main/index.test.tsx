import React from 'react';
import '@testing-library/jest-dom';
import { render, screen } from '@testing-library/react';
import Home from '@/app/page';

describe('Home page (temp test)', () => {
  it ('Should render Home stub correct', () => {
    render(<Home />);

    const navHeaders = screen.getAllByRole('heading');
    const needTextHeader = 'Docs';

    expect(navHeaders[0]).toHaveTextContent(needTextHeader);
  });
});
